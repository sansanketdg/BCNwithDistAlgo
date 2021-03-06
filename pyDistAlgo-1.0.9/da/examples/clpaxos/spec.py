# -*- generated by 1.0.9 -*-
import da
PatternExpr_211 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern214_'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern('a')])
PatternExpr_244 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern247_'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern(None)])
PatternExpr_274 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern277_'), da.pat.BoundPattern('_BoundPattern278_'), da.pat.BoundPattern('_BoundPattern279_'), da.pat.FreePattern('a')])
PatternExpr_329 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.BoundPattern('_BoundPattern332_'), da.pat.BoundPattern('_BoundPattern333_'), da.pat.FreePattern('a')])
PatternExpr_416 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern(None)])
PatternExpr_445 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.BoundPattern('_BoundPattern448_'), da.pat.BoundPattern('_BoundPattern449_'), da.pat.FreePattern('a')])
PatternExpr_473 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoB'), da.pat.BoundPattern('_BoundPattern476_'), da.pat.BoundPattern('_BoundPattern477_')])
PatternExpr_508 = da.pat.TuplePattern([da.pat.ConstantPattern('Done')])
PatternExpr_513 = da.pat.BoundPattern('_BoundPattern514_')
PatternExpr_529 = da.pat.TuplePattern([da.pat.ConstantPattern('Prepare'), da.pat.FreePattern('n'), da.pat.FreePattern('p')])
PatternExpr_548 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.FreePattern('vpn'), da.pat.FreePattern('vv'), da.pat.SelfPattern()])
PatternExpr_600 = da.pat.TuplePattern([da.pat.ConstantPattern('OneC'), da.pat.FreePattern('n'), da.pat.FreePattern('v'), da.pat.FreePattern('p')])
PatternExpr_624 = da.pat.TuplePattern([da.pat.ConstantPattern('TwoAv'), da.pat.BoundPattern('_BoundPattern627_'), da.pat.FreePattern(None), da.pat.SelfPattern()])
PatternExpr_664 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.FreePattern('n'), da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_702 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern705_'), da.pat.FreePattern('vn'), da.pat.FreePattern('vv'), da.pat.FreePattern(None)])
PatternExpr_732 = da.pat.TuplePattern([da.pat.ConstantPattern('Promise'), da.pat.BoundPattern('_BoundPattern735_'), da.pat.BoundPattern('_BoundPattern736_'), da.pat.BoundPattern('_BoundPattern737_'), da.pat.FreePattern('a')])
PatternExpr_480 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.FreePattern(None)]), da.pat.TuplePattern([da.pat.ConstantPattern('TwoB'), da.pat.BoundPattern('_BoundPattern490_'), da.pat.BoundPattern('_BoundPattern491_')])])
PatternExpr_515 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern521_')]), da.pat.TuplePattern([da.pat.ConstantPattern('Done')])])
_config_object = {}
import sys

class Proposer(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ProposerReceivedEvent_0 = []
        self._ProposerReceivedEvent_1 = []
        self._ProposerReceivedEvent_2 = []
        self._ProposerReceivedEvent_3 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_0', PatternExpr_211, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_1', PatternExpr_244, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_2', PatternExpr_274, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ProposerReceivedEvent_3', PatternExpr_329, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, quorumsize, f, nrounds, timeout, **rest_906):
        super().setup(acceptors=acceptors, quorumsize=quorumsize, f=f, nrounds=nrounds, timeout=timeout, **rest_906)
        self._state.acceptors = acceptors
        self._state.quorumsize = quorumsize
        self._state.f = f
        self._state.nrounds = nrounds
        self._state.timeout = timeout
        self._state.propNum = (0, self._id)
        self._state.propVal = self._id

    def run(self):
        count = 0
        while (count < self._state.nrounds):
            self.work()
            super()._label('prepare', block=False)
            self.send(('Prepare', self._state.propNum, self._id), to=self._state.acceptors)
            super()._label('_st_label_206', block=False)
            _st_label_206 = 0
            self._timer_start()
            while (_st_label_206 == 0):
                _st_label_206 += 1
                if (len({a for (_, _, (_ConstantPattern229_, _BoundPattern231_, _, _, a)) in self._ProposerReceivedEvent_0 if (_ConstantPattern229_ == 'Promise') if (_BoundPattern231_ == self._state.propNum)}) > self._state.quorumsize):
                    super()._label('propose', block=False)
                    (_, voted) = max(({(n, v) for (_, _, (_ConstantPattern263_, _BoundPattern265_, n, v, _)) in self._ProposerReceivedEvent_1 if (_ConstantPattern263_ == 'Promise') if (_BoundPattern265_ == self._state.propNum) if (len({a for (_, _, (_ConstantPattern292_, _BoundPattern294_, _BoundPattern295_, _BoundPattern296_, a)) in self._ProposerReceivedEvent_2 if (_ConstantPattern292_ == 'Promise') if (_BoundPattern294_ == self._state.propNum) if (_BoundPattern295_ == n) if (_BoundPattern296_ == v)}) > self._state.f)} | {(((- 1), self._id), self._state.propVal)}))
                    self.send(('OneC', self._state.propNum, voted, self._id), to=self._state.acceptors)
                    super()._label('_st_label_324', block=False)
                    _st_label_324 = 0
                    self._timer_start()
                    while (_st_label_324 == 0):
                        _st_label_324 += 1
                        if (len({a for (_, _, (_ConstantPattern346_, _BoundPattern348_, _BoundPattern349_, a)) in self._ProposerReceivedEvent_3 if (_ConstantPattern346_ == 'TwoAv') if (_BoundPattern348_ == self._state.propNum) if (_BoundPattern349_ == voted)}) > self._state.quorumsize):
                            super()._label('end', block=False)
                            self.output(('Succeeded proposing %s' % (voted,)))
                            count += 1
                            continue
                            _st_label_324 += 1
                        elif self._timer_expired:
                            self.output('Failed to Propose in time, retrying.')
                            _st_label_324 += 1
                        else:
                            super()._label('_st_label_324', block=True, timeout=self._state.timeout)
                            _st_label_324 -= 1
                    else:
                        if (_st_label_324 != 2):
                            continue
                    if (_st_label_324 != 2):
                        break
                    _st_label_206 += 1
                elif self._timer_expired:
                    self.output('Failed to Prepare in time, retrying.')
                    _st_label_206 += 1
                else:
                    super()._label('_st_label_206', block=True, timeout=self._state.timeout)
                    _st_label_206 -= 1
            else:
                if (_st_label_206 != 2):
                    continue
            if (_st_label_206 != 2):
                break
            self._state.propNum = ((self._state.propNum[0] + 1), self._id)
        self.send(('Done',), to=self._state.acceptors)

class Acceptor(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._AcceptorReceivedEvent_0 = []
        self._AcceptorReceivedEvent_1 = []
        self._AcceptorSentEvent_2 = []
        self._AcceptorReceivedEvent_3 = []
        self._AcceptorSentEvent_5 = []
        self._AcceptorSentEvent_7 = []
        self._AcceptorSentEvent_8 = []
        self._AcceptorReceivedEvent_9 = []
        self._AcceptorReceivedEvent_10 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_0', PatternExpr_416, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_1', PatternExpr_445, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_2', PatternExpr_473, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_3', PatternExpr_508, sources=[PatternExpr_513], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_4', PatternExpr_529, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_528]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_5', PatternExpr_548, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_6', PatternExpr_600, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Acceptor_handler_599]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_7', PatternExpr_624, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.SentEvent, '_AcceptorSentEvent_8', PatternExpr_664, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_9', PatternExpr_702, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_AcceptorReceivedEvent_10', PatternExpr_732, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, acceptors, proposers, quorumsize, f, **rest_906):
        super().setup(acceptors=acceptors, proposers=proposers, quorumsize=quorumsize, f=f, **rest_906)
        self._state.acceptors = acceptors
        self._state.proposers = proposers
        self._state.quorumsize = quorumsize
        self._state.f = f
        self._state.peers = (self._state.acceptors | self._state.proposers)

    def run(self):
        while True:
            super()._label('_st_label_413', block=False)
            v = n = a = None

            def ExistentialOpExpr_414():
                nonlocal v, n, a
                for (_, _, (_ConstantPattern434_, n, v, _)) in self._AcceptorReceivedEvent_0:
                    if (_ConstantPattern434_ == 'TwoAv'):
                        if ((len({a for (_, _, (_ConstantPattern462_, _BoundPattern464_, _BoundPattern465_, a)) in self._AcceptorReceivedEvent_1 if (_ConstantPattern462_ == 'TwoAv') if (_BoundPattern464_ == n) if (_BoundPattern465_ == v)}) > self._state.quorumsize) and (not PatternExpr_480.match_iter(self._AcceptorSentEvent_2, _BoundPattern490_=n, _BoundPattern491_=v, SELF_ID=self._id))):
                            return True
                return False
            p = None

            def UniversalOpExpr_500():
                nonlocal p
                for p in self._state.proposers:
                    if (not PatternExpr_515.match_iter(self._AcceptorReceivedEvent_3, _BoundPattern521_=p, SELF_ID=self._id)):
                        return False
                return True
            _st_label_413 = 0
            while (_st_label_413 == 0):
                _st_label_413 += 1
                if ExistentialOpExpr_414():
                    self.send(('TwoB', n, v), to=self._state.peers)
                    _st_label_413 += 1
                elif UniversalOpExpr_500():
                    break
                    _st_label_413 += 1
                else:
                    super()._label('_st_label_413', block=True)
                    _st_label_413 -= 1
            else:
                if (_st_label_413 != 2):
                    continue
            if (_st_label_413 != 2):
                break

    def maxpromised(self):
        return max(({n for (_, _, (_ConstantPattern682_, n, _, _, _)) in self._AcceptorSentEvent_8 if (_ConstantPattern682_ == 'Promise')} | {((- 2), self._id)}))

    def islegal(self, n, v):
        voted = {(vn, vv) for (_, _, (_ConstantPattern721_, _BoundPattern723_, vn, vv, _)) in self._AcceptorReceivedEvent_9 if (_ConstantPattern721_ == 'Promise') if (_BoundPattern723_ == n) if (len({a for (_, _, (_ConstantPattern750_, _BoundPattern752_, _BoundPattern753_, _BoundPattern754_, a)) in self._AcceptorReceivedEvent_10 if (_ConstantPattern750_ == 'Promise') if (_BoundPattern752_ == n) if (_BoundPattern753_ == vn) if (_BoundPattern754_ == vv)}) > self._state.f)}
        if (voted and (not (max(voted)[1] is None))):
            return (v == max(voted)[1])
        else:
            return True

    def _Acceptor_handler_528(self, n, p):
        if (n > self.maxpromised()):
            (vn, vv) = max(({(vpn, vv) for (_, _, (_ConstantPattern567_, vpn, vv, _ConstantPattern571_)) in self._AcceptorSentEvent_5 if (_ConstantPattern567_ == 'TwoAv') if (_ConstantPattern571_ == self._id)} | {(((- 1), self._id), None)}))
            self.send(('Promise', n, vn, vv, self._id), to=self._state.peers)
    _Acceptor_handler_528._labels = None
    _Acceptor_handler_528._notlabels = None

    def _Acceptor_handler_599(self, n, v, p):

        def ExistentialOpExpr_622():
            for (_, _, (_ConstantPattern641_, _BoundPattern643_, _, _ConstantPattern645_)) in self._AcceptorSentEvent_7:
                if (_ConstantPattern641_ == 'TwoAv'):
                    if (_BoundPattern643_ == n):
                        if (_ConstantPattern645_ == self._id):
                            if True:
                                return True
            return False
        if ((n >= self.maxpromised()) and self.islegal(n, v) and (not ExistentialOpExpr_622())):
            self.send(('TwoAv', n, v, self._id), to=self._state.peers)
    _Acceptor_handler_599._labels = None
    _Acceptor_handler_599._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        nproposers = (int(sys.argv[1]) if (len(sys.argv) > 1) else 5)
        nacceptors = (int(sys.argv[2]) if (len(sys.argv) > 2) else 10)
        nrounds = (int(sys.argv[3]) if (len(sys.argv) > 3) else 1)
        timeout = (int(sys.argv[4]) if (len(sys.argv) > 4) else 1)
        f = int(((nacceptors - 1) / 3))
        quorum = int(((nacceptors / 2) + f))
        acceptors = self.new(Acceptor, num=nacceptors)
        proposers = self.new(Proposer, num=nproposers)
        self._setup(acceptors, (acceptors, proposers, quorum, f))
        self._setup(proposers, (acceptors, quorum, f, nrounds, timeout))
        self._start(acceptors)
        self._start(proposers)
