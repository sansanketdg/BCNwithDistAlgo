# -*- generated by 1.0.9 -*-
import da
PatternExpr_182 = da.pat.TuplePattern([da.pat.ConstantPattern('execute'), da.pat.FreePattern('replica_index')])
PatternExpr_189 = da.pat.FreePattern('client1')
_config_object = {}
import sys

class Replica(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_0', PatternExpr_182, sources=[PatternExpr_189], destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_181])])

    def setup(self, olympus, client, list_replicas, config, **rest_237):
        super().setup(olympus=olympus, client=client, list_replicas=list_replicas, config=config, **rest_237)
        self._state.olympus = olympus
        self._state.client = client
        self._state.list_replicas = list_replicas
        self._state.config = config
        self._state.terminate = False

    def run(self):
        self.output('Started Replica...waiting for an operations...')
        super()._label('_st_label_235', block=False)
        _st_label_235 = 0
        while (_st_label_235 == 0):
            _st_label_235 += 1
            if self._state.terminate:
                _st_label_235 += 1
            else:
                super()._label('_st_label_235', block=True)
                _st_label_235 -= 1

    def _Replica_handler_181(self, replica_index, client1):
        self.output('Received request from Client for task execution')
        print('Replica i received - ', replica_index)
        ind = int(replica_index)
        if (ind == 2):
            self.send(('execution_success', '10'), to=self._state.client)
        else:
            ind += 1
            self.send(('execute', str(ind)), to=self._state.list_replicas[ind])
        self._state.terminate = True
    _Replica_handler_181._labels = None
    _Replica_handler_181._notlabels = None
