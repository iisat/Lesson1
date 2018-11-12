import cProfile
import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

#test_fib(fib)

#cProfile.run('fib(10)')     177/1    0.000    0.000    0.000    0.000 lesson.py:3(fib)
#cProfile.run('fib(15)')     1973/1    0.001    0.000    0.001    0.001 lesson.py:3(fib)
#cProfile.run('fib(20)')     1973/1    0.001    0.000    0.001    0.001 lesson.py:3(fib)

#python -m timeit -n 100 -s "import lesson" "lesson.fib(10)"

# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(10)"
# 100 loops, best of 5: 31.4 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(15)"
# 100 loops, best of 5: 361 usec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(20)"
# 100 loops, best of 5: 4.08 msec per loop

#Decorator
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(10)"
# 100 loops, best of 5: 402 nsec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(15)"
# 100 loops, best of 5: 160 nsec per loop
# (venv) C:\Users\user\PycharmProjects\Lesson1\Lesson4>python -m timeit -n 100 -s "import lesson" "lesson.fib(20)"
# 100 loops, best of 5: 160 nsec per loop
