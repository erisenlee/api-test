from celery import Celery


app = Celery('test',backend='redis://localhost/3',broker='redis://localhost/4')

@app.task
def add(x, y):
    return x + y
    
    

