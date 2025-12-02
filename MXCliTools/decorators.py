from functools import wraps
import time
import sys
import io

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting function")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Function completed in {run_time:.4f} seconds")
        return result
    
    return wrapper

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts:
                        print(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def confirm(prompt="Are you sure? (y/N): "):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = input(prompt).strip().lower()
            if response in ('y', 'yes'):
                return func(*args, **kwargs)
            else:
                print("Operation cancelled.")
                return None
        return wrapper
    return decorator

def log_args(logger=print):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            logger(f"{func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

def show_progress(symbol="▰"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running {func.__name__}... ", end="", flush=True)
            for _ in range(5):
                print(symbol, end="", flush=True)
                time.sleep(0.2)
            print(" Done!")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache():
    cache_dict = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key in cache_dict:
                print(f"Using cached result for {func.__name__}")
                return cache_dict[key]
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
        return wrapper
    return decorator

def silent():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with io.StringIO() as buf:
                sys.stdout = buf
                sys.stderr = buf
                try:
                    result = func(*args, **kwargs)
                finally:
                    sys.stdout = sys.__stdout__
                    sys.stderr = sys.__stderr__
            return result
        return wrapper
    return decorator