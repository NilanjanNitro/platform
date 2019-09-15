# test.py
from fluent import event
from fluent import sender

sender.setup('fluentd.test', host='localhost', port=24224)
event.Event('follow', {'function': 'tenant_constructor', 'status': 'Object initialized'})
