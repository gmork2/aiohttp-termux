import json
import logging

DEFAULT_METHODS = ('POST', 'GET')


class BaseCommandView:
    def __init__(self):
        self.methods = {}

        for method_name in DEFAULT_METHODS:
            method = getattr(self, method_name.lower(), None)
            if method:
                self.register_method(method_name, method)

    def register_method(self, method_name, method):
        self.methods[method_name.upper()] = method


class CommandView(BaseCommandView):
    def __init__(self, resource):
        super().__init__()
        self.resource = resource
