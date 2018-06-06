from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: pretty
    type: stdout
    short_description: prettified unixy callback
    description:
      - Yet another prettified callback
    version_added: "2.5"
    requirements:
      - set as stdout in configuration
'''

from ansible import constants as C
from ansible.plugins.callback.unixy import CallbackModule as CallbackModule_unixy


class CallbackModule(CallbackModule_unixy):  # pylint: disable=too-few-public-methods,no-init
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'pretty'

    def get_prefix(self, msg):
        return {
            'ok': '✔',
            'done': '✔',
            'unreachable': '✘',
            'failed': '✘',
        }.get(msg, '?')

    def v2_playbook_on_task_start(self, task, is_conditional):
        args = ''
        if not task.no_log and C.DISPLAY_ARGS_TO_STDOUT:
            args = u', '.join(u'%s=%s' % a for a in task.args.items())
            args = u' %s' % args

        self._display.display("\033[1m\033[96m➤ {}... {}\033[0m".format(task.get_name().strip(), args))

    def _process_result_output(self, result, msg):
        host = result._host.get_name()
        prefix = self.get_prefix(msg)
        output = "{} {} {}".format(prefix, host, msg)
        if self._run_is_verbose(result):
            output = "{} {} {}: {}".format(prefix, host, msg, self._dump_results(result._result, indent=4))

        if self.delegated_vars:
            task_delegate_host = self.delegated_vars['ansible_host']
            output = "{} {} -> {} {}".format(prefix, host, task_delegate_host, msg)

        if result._result.get('msg') and result._result.get('msg') != "All items completed":
            output = "{}: {}".format(output, result._result.get('msg'))

        if result._result.get('stdout'):
            output = "{} | stdout: {}".format(output, result._result.get('stdout'))

        if result._result.get('stderr'):
            output = "{} | stderr: {}".format(output, result._result.get('stderr'))

        return output
