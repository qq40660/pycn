# -*- coding: utf-8 -*-
'''
:bugto: inpool@gmail.com 

logging 模块提供一些类和方法用于为应用或类库实现松散的事件日志系统
'''

NOTSET = 0
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

class Logger(object):
    '''
    Logger 类必须通过 logging.getLogger() 模块函数实例化    
    '''
    
    def __init__(self, name, level=0):
        '''
        初始化 Logger 实例。设置 self.propagate 。
        当 self.propagate 值为 False 时，当前实例的日志 record 不向 Logger 树的
        上级结点传递 
        
        -name: 当前实例的 name
        -level: 当前实例的 level 临界值
        '''
        self.propagate = 1
    
    def setlevel(self, lvl):
        '''
        设置临界值 level ，所有比 level 级别小的日志消息将被禁止输出。默认值为
        logging.NOTSET 。 RootLogger 的默认值为 logging.WARNING
        
        -lvl: 要设置的目标 level
        '''
    
    def isEnableFor(self, lvl):
        '''
        通过计算判断当前实例的 level 级日志是否允许输出。
        
        -lvl: 要检测的目标 level
        '''
        
    def getEffectiveLevel(self):
        '''
        通过计算返回当前实例的实际有效 level 值
        '''
        
    def getChild(self, suffix):
        '''
        logging.getLoger 的扩展写法，获取当前 Logger 实例的子 Logger，在当前
        Logger 的 name 来自 __name__ 等变量时较有用
        
        -suffix: 子 Loger 的名字，去掉当前 Logger 实例名字的前缀
        '''
        
    def debug(self, msg, *args, **kwargs):
        '''
        记录一条 logging.DEBUG 级别的日志消息。最终将以 msg % args 解析值。
        
        -msg: 为消息的字符串格式。
        -args: 当 msg 是字典格式化字符串时， args 必须为字典类型，
             : 否则应该为对应个数的值，
        -kwargs: 有两个可设置的选项: exc_info 和 extra
            -exc_info: 默认为 False 。当 exc_info 不为 False 时，会有一个
                     : 异常消息被附加到 message 之后。当提供的值为异常元组
                     : （类似 sys.exc_info 的返回值）时，将使用这个元组格式
                     : 化 异常信息，否则调用 sys.exc_info 生成。
            -extra: 一个字典，用来替换 format（来自 basicConfig 或 Formatter）
                  : 中的自定义变量。extra 必须包含所有自定义变量
        '''

    def warning(self, msg, *args, **kwargs):
        '''
        记录一条 logging.WARNING 级别的日志消息。各参数参加 self.debug()
        '''

    def error(self, msg, *args, **kwargs):
        '''
        记录一条 logging.ERROR 级别的日志消息。各参数参加 self.debug()
        '''

    def critical(self, msg, *args, **kwargs):
        '''
        记录一条 logging.CRITICAL 级别的日志消息。各参数参加 self.debug()
        '''

    def log(self, lvl, msg, *args, **kwargs):
        '''
        记录一条 lvl 级别的日志消息。各参数参加 self.debug()
        '''
        
    def exception(self, msg, *args):
        '''
        记录1条 logging.ERROR 级别的日志，异常信息被附加到消息之后。其余参数参考
        self.debug()
        该方法应该只在异常处理时调用
        '''
        
    def addFilter(self, filt):
        '''
        向当前实例添加指定过滤器 filt
        '''

    def removeFilter(self, filt):
        '''
        从当前实例删除指定过滤器 filt        
        '''

    def filter(self, record):
        '''
        根据当前实例的 filters 设置，判读 record 是否会被通过处理。能通过则返回
        True 否则返回 False
        '''
    
    def addHandler(self, hdlr):
        '''
        向当前实例添加 Handler 处理器
        '''
        
    def removeHandler(self, hdlr):
        '''
        从当前实例删除 Handler 处理器
        '''
        
    def findCaller(self): 
        '''
        若某 callableA 调用了findCaller，则任意其他 callableB 可调用
        callableA 获得 callableB的调用信息
        '''
    
    def handler(self, record):
        '''
        将 record 提交给所有当前实例所关联的 handler 处理。record 会根据 Logger
        树每个节点的 propagate 值判断是否向上级传递
        '''
        
    def makeRecord(self, name, lvl, fn, lno, msg,
                   exc_info, func=None, extra=None):
        '''
        创建 Record 的工厂函数，可由子类覆盖，以创建自定义的 record
        '''
    
        
class Handler(object):
    '''
    Handler 类不可直接实例化， 只是扮演基类角色，所有 Handler 的子类必须调用
    Hanlder.__init__() 进行初始化。
    '''
    
    def __init__(self, level=NOTSET):
        '''
        初始化实例，设置 level ，创建空的 filter 列表，创建 I/O 进程锁
        '''
        
    def createLock(self):
        '''
        创建 I/O 进程锁，控制对非线程安全 I/O 接口的访问
        '''
        
    def acquire(self):
        '''
        获取由 createLock 创建的 I/O 进程锁
        '''
        
    def release(self):
        '''
        释放由 acquire 获取的 I/O 进程锁
        '''
        
    def setLevel(self):
        '''
        设置当前 Handler 实例的 level 临界值。
        '''
        
    def setFormatter(self, form):
        '''
        设置当前实例的 Formatter。
        '''

    def addFilter(self, filt):
        '''
        向当前实例添加过滤器
        '''
        
    def removeFilter(self, filt):
        '''
        从当前实例移除过滤器
        '''
        
    def filter(self, record):
        '''
        根据当前实例的 filters 设置，判读 record 是否会被通过处理。能通过则返回
        True 否则返回 False
        '''
        
    def flush(self):
        '''
        立即输出所有日志信息，该方法不做任何事，子类必须重新实现。
        '''
        
    def close(self):
        '''
        该方法不作任何输出，仅释放当前实例所占用的所有资源，并将当前实例从日志系统
        内部 Handlers 列表中删除。子类重写该方法时必须调用该方法
        '''
        
    def handle(self, record):
        '''
        根据当前实例的过滤器设置有条件的处理 record ，对处理的 record 使用 I/O 线
        程锁的 acquire 和 release 包裹。若处理，则返回1，否则返回0
        '''
        
    def handleError(self, record):
        '''
        There is no cndoc!
        '''
        
    def format(self, record):
        '''
        格式化 record 。如果设置了 formatter ，则使用 formatter 。否则使用默认的
        formatter （%(message)s）。
        '''
        
    def emit(self, record):
        '''
        无条件处理 record
        '''
        
        
class Formatter(object):
    '''
    Formatter 类用于格式化 LogRecord。 字典属性详见 LogRecord 的属性 。
    '''
    
    def __init__(self, fmt=None, datefmt=None):
        '''
        fmt 和 datefmt 为消息和日期的格式化字符串。若未指定，则 fmt 默认为
        '%(message)s'， datefmt 默认为 ISO8601
        '''
        
    def format(self, record):
        '''
        将 record 格式化为字符串。若 fmt 包含 '%(asctime)s' ，则使用 datefmt 格
        式化事件发生的时间。若存在异常信息，则使用 formatException 格式化异常信息
        并附在后面。
        '''
    
    def formatTime(self, record, datefmt=None): 
        '''
        用于 format 方法调用， 子类可以重写该方法以实现特殊需求。默认动作为调用
        time.strftime 格式化。当 datefmt 未设置时。默认为 ISO8601
        '''
        
    def formatException(self, exc_info):
        '''
        将指定的异常信息（与 sys.exc_info() 的返回结果类似的标准异常元组）格式化为
        字符串。默认动作为仅仅使用 traceback.print_exception() 函数的返回结果。
        格式化后的字符串会被缓存在exc_text。编写 Formatter 的子类时，若覆盖了该方
        法，须确保每次调用后清除缓存，以保证调用时重新计算而不是调用了错误的缓存。
        '''
        
        
class Filter(object):
    '''
    Filter 类赋予 Handler 和 Logger 比日志级别更精细的控制。
    '''
    
    def __init__(self, name=''):
        '''
        初始化 Filter 时，提供一个以 '.' 分隔的名字，表示 Logger 树的一个节点，该
        节点及其子节点的 Logger 发出的日志消息将被通过，其他的日志消息一律被阻止。
        当 name 为空字符串时，允许所有的日志消息通过。
        '''
        
    def filter(self, record):
        '''
        判断指定 record 是否允许通过当前过滤器，不允许时返回0，允许时返回非0
        '''
        
        
class LogRecord(object):
    '''
    '''