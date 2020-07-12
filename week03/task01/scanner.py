"""
__author__:'vacada'
__description__:'编写基于多进程或多线程模型的主机扫描器'`
__mtime__:2020/7/10
"""
import argparse     # 命令行参数解析
import socket
import re
import os
import json
from time import time
from multiprocessing import cpu_count                   # CPU核数
from multiprocessing.pool import Pool                   # 进程池
from concurrent.futures import ThreadPoolExecutor       #
from pythonping import ping   # ping测试


PORT = '8080-8086'

class Scanner():
    """主机扫描器基本业务"""
    def __init__(self):
        self.args = None
        self.port = '1-10'
        self.ip = None
    
    # 定义命令行参数
    def command_analysis(self):
        parser = argparse.ArgumentParser(description='主机扫描器')
        parser.add_argument('-n', type=int, help='并发数量')
        parser.add_argument('-f', type=str, choices=['ping', 'tcp'], help='测试类型')
        parser.add_argument('-ip', type=str, help='IP地址，支持192.168.0.1-192.168.0.100或-ip 192.168.0.1格式')
        parser.add_argument('-w', action='store_true', help='保存扫描结果')
        parser.add_argument('-m', type=str, choices=['proc', 'thread'], help='选择多进程或多线程模型')
        parser.add_argument('-v', action='store_true', help='统计耗时')    
        args = parser.parse_args()

        if not args.n:
            print('请输入并发数量，如：-n 4')
        elif not args.f:
            print(args.n)
            print('请选择[ping]测试或[tcp]测试，如：-f ping')
        elif not args.ip:
            print('请输入IP地址，如：-ip 192.168.0.1-192.168.0.100或-ip 192.168.0.1')
        else:
            self.args = args
    
    # 检查IP是否合法
    def check_ip(self):
        ip = self.args.ip
        # IPV4 正则匹配表达式
        compile_ip=re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')

        if ip.count('-') == 1 and self.args.f == 'ping':
            ips = ip.split('-')
            if ips[0] < ips[1] and None not in list(map(lambda x : compile_ip.match(x), ips)):
                # self.ip = ips 
                return ips   
            else: 
                return False
        elif ip.count('-') == 0:
            if compile_ip.match(ip):
                # self.ip = ip
                return ip   
            else:    
                return False
        else:
            return False

    # ping测试  
    def check_ping(self, ip):
        # print("%s子进程开始，进程ID：%d" % (ip, os.getpid())
        ip_ping = ping(ip)
        if str(ip_ping).count('Reply') == 4:
            # print('ip执行完成')
            # return (ip, ip_ping)
            return ip
        
    # tcp端口测试
    def check_port(self, ip, port):
        # print("%s子进程开始，进程ID：%d" % (port, os.getpid()))
        try:
            #socket.AF_INET 服务器之间网络通信
            #socket.SOCK_STREAM  流式socket , 当使用TCP时选择此参数
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            return port
        except Exception as e:
            print("{port}失败了，原因是：{e}".format(port=port, e=e))
        finally:
            s.close()    


class ProcessModel():
    """多进程模式"""
    def __init__(self):
        self.cpu_count = cpu_count()
    
    # 多进程ping操作
    def create_ping(self, run_function, n, ip_start, ip_stop):
        p = Pool(n)
        ip_done = []
        if n > self.cpu_count:
            p = p = Pool(self.cpu_count)
        for i in range(int(ip_start[-1]), int(ip_stop[-1])+1):
            ip = ip_start[0] + '.' + str(i)
            result = p.apply_async(run_function, args=(ip,))
            ip_done.append(result)
        p.close()
        p.join()
        p.terminate()

        return ip_done

    # 多进程tcp操作
    def creare_port(self, run_function, n, ip_result, port_scope):
        p = Pool(n)
        port_done = []
        if n > self.cpu_count:
            p = p = Pool(self.cpu_count)
        for i in range(int(port_scope[0]), int(port_scope[1])+1):
            result = p.apply_async(run_function, args=(ip_result, i,))
            port_done.append(result)
        p.close()
        p.join()
        p.terminate()

        return port_done


class ThreadModel():
    """多线程模式"""

    # 多线程ping操作
    def thread_ping(self, run_function, n, ip_start, ip_stop):
        ip_ls = []
        for i in range(int(ip_start[-1]), int(ip_stop[-1])+1):
            ip = ip_start[0] + '.' + str(i)
            ip_ls.append(ip)

        with ThreadPoolExecutor(max_workers=5) as executor:
            ping_done = [executor.submit(run_function, ip) for ip in ip_ls]
            # print([obj.result() for obj in ping_done])

        return ping_done

    # 多线程tcp操作
    def thread_tcp(self, run_function, n, ip_result, port_scope):
        port_ls = []
        for i in range(int(port_scope[0]), int(port_scope[1])+1):
            port_ls.append(i)

        with ThreadPoolExecutor(max_workers=5) as executor:
            port_done = [executor.submit(run_function, ip_result, port) for port in port_ls]
            # print([obj.result() for obj in ping_done])

        return port_done


# class TimeConsuming():
#     def __init__():
#         pass

#     def time_start(self):
        

#     def time_stop(self):
#         pass


class DataStorage():
    pass


if __name__ == "__main__":
    time_start = time()
    scanner = Scanner()
    proc = ProcessModel()
    thre = ThreadModel()
    scanner.command_analysis()
    ip_result = scanner.check_ip()
    # 对IP进行ping或tcp检测
    result = {}
    success_data = []
    # print(scanner.args)
    if type(ip_result) == list:
        """IP段 ping测试"""
        ip_start= ip_result[0].rsplit('.', 1)
        ip_stop= ip_result[1].rsplit('.', 1)
        if ip_start[0] == ip_stop[0]:
            # 进程执行ping操作
            if scanner.args.m == 'proc':
                ping_result = proc.create_ping(scanner.check_ping, scanner.args.n, ip_start, ip_stop)
                # 获取ping成功的IP
                for i in ping_result:
                    # print(i.get())
                    success_data.append(i.get())
                result['ping_process'] = success_data
            # 线程执行ping操作
            elif scanner.args.m == 'thread':
                ping_thread = thre.thread_ping(scanner.check_ping, scanner.args.n, ip_start, ip_stop)
                # print([obj.result() for obj in ping_thread])
                for obj in ping_thread:
                    success_data.append(obj.result())
                result['ping_thread'] = success_data
            else:
                # 不并发执行
                for i in range(int(ip_start[-1]), int(ip_stop[-1])+1):
                    ip = ip_start[0] + '.' + str(i)
                    ping_result = scanner.check_ping(ip)
                    # print(ping_result)
                    success_data.append(ping_result)
                    result['ping_success'] = success_data
        else:
            print('IP参数不合法')
    elif type(ip_result) == str and scanner.args.f == 'ping':
        """单一IP ping测试"""
        ping_result = scanner.check_ping(ip_result)
        # print(ping_result)
        success_data.append(ping_result)
        result['ping_ip'] = success_data
    elif type(ip_result) == str and scanner.args.f == 'tcp':
        """单一IP tcp测试"""
        port_scope = PORT.split('-')
        # port_list = []
        # 进程执行tcp操作
        if scanner.args.m == 'proc':
            port_result = proc.creare_port(scanner.check_port, scanner.args.n, ip_result, port_scope)
            # 获取ping成功的IP
            for i in port_result:
                if i.get() != None:
                    # print(i.get())
                    success_data.append(i.get())
            result['tcp_process'] = success_data
        # 线程执行tcp操作
        elif scanner.args.m == 'thread':
            port_thread = thre.thread_tcp(scanner.check_port, scanner.args.n, ip_result, port_scope)
            print([obj.result() for obj in port_thread])
            for obj in port_thread:
                if obj.result() != None:
                    success_data.append(obj.result())
            result['tcp_thread'] = success_data
        else:
            # 不并发执行
            for i in range(int(port_scope[0]), int(port_scope[1])+1):
                port_relust = scanner.check_port(ip_result, i)
                if port_relust != None:
                    success_data.append(str(port_relust))
            result['tcp_success'] = success_data      
    else:
        print('IP参数不合法')

    time_end = time()
    # 统计耗时
    if scanner.args.v:
        # print(time_start, time_end)
        print(f'扫描器耗时：%s' %(time_end-time_start))
        result['time'] = time_end-time_start
    
    # 汇总信息
    results = {}
    # scanner.agrs转字典后赋值
    results['send']= vars(scanner.args)     
    results['come_back'] = result     
    print(results)

    # 保存至json文件
    if scanner.args.w:
        with open("../task01/scanner-data.json", 'w') as f:
            json.dump(results, f)
            print('文件写入完成')