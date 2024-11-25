import contextlib


# 上下文管理器协议
@contextlib.contextmanager
def fileopen(filename):
    # 前置,预置内容
    print("file open")
    yield {
        print("Hello")
    }
    # 后置内容
    print("file end")


with fileopen('./wabg.txt') as f:
    print('File processing')
