import time

def time_profiler(func: callable) -> callable:
    """Se pasa una función o método para medir el tiempo que toma una función o método en ejecutarse.
        Para utilizarse, decorar la función o método con esta misma.

    Args:
        func (callable): función a hacer time profile.

    Return:
        tuple[tiempo en nanosegundos, return de la función en sí]
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        fun_return = func(*args, **kwargs)
        final = time.perf_counter_ns()
        time_result = final - start
        print(f'Ejecutado en: {time_result} ns')
        return fun_return
    
    return wrapper

# todo: logger?