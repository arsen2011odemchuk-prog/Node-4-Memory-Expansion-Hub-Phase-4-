this is only sarter code wil be ipmroven when everything is get builded up

import torch
import time
import pynvml  # Для мониторинга температуры и памяти 24/7

def init_node():
    print("--- HEX-Node 4: AI Compute Initialization ---")
    
    # 1. Проверка GPU (RTX 3060)
    if not torch.cuda.is_available():
        print("[ERROR] CUDA not found. Check NVIDIA Drivers!")
        return False
    
    gpu_name = torch.cuda.get_device_name(0)
    vram_total = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"[OK] Found GPU: {gpu_name}")
    print(f"[OK] Total VRAM: {vram_total:.2f} GB")
    
    # Инициализация NVML для мониторинга
    pynvml.nvmlInit()
    return True

def monitor_system():
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
    mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
    print(f"[MONITOR] Temp: {temp}°C | VRAM Used: {mem_info.used / 1e6:.1f}MB")
    return temp

def run_inference_loop():
    # Создаем фиктивную нейросеть для теста (нагружаем тензорные ядра)
    print("[SYSTEM] Loading model into VRAM...")
    device = torch.device("cuda")
    model = torch.nn.Linear(10000, 10000).to(device)
    data = torch.randn(100, 10000).to(device)

    print("[SYSTEM] Starting 24/7 Inference Loop...")
    try:
        while True:
            # Симуляция вычислений ИИ
            output = model(data)
            
            # Мониторинг каждые 10 секунд
            temp = monitor_system()
            
            # Защита от перегрева (Throttling)
            if temp > 82:
                print("[WARNING] Temperature high! Cooling down...")
                time.sleep(30)
            
            time.sleep(10)
    except KeyboardInterrupt:
        print("[STOP] Node 4 manually stopped.")

if __name__ == "__main__":
    if init_node():
        run_inference_loop()
