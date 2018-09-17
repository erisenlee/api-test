from apitest import celery_app
# from celery import shared_task
@celery_app.task
def add(x, y):
    return x + y
    

@celery_app.task(bind=True)
def dump_context(self, x, y):
    print('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(
            self.request))




if __name__ == '__main__':
    add.delay(10,20)