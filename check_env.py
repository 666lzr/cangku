import sys
import torch
def environment_check():
    print("===== 环境检测信息 =====")
    # 1. Python 版本
    print(f"1. Python 版本: {sys.version}")
    # 2. PyTorch 版本
    print(f"2. PyTorch 版本: {torch.__version__}")
    # 3. 是否支持 CUDA
    cuda_available = torch.cuda.is_available()
    print(f"3. CUDA 是否可用: {cuda_available}")
    # 4. 创建 3×3 随机张量并打印
    print("4. 3×3 随机张量:")
    rand_tensor = torch.rand(3, 3)
    print(rand_tensor)
if __name__ == "__main__":
    environment_check()