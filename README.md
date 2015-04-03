# sangwook-openstack-ml2-driver
Openstack ML2 Driver Test

## 목적

- OpenStack 의 Neutron 을 이해하고, ML2 Driver 를 이해하기 위함.
- 그래서 단순히 로그만 출력하는 ML2 Driver 를 한 번 만들어 보는 것이 목적임.

## 설치

- 패키지를 설치하고,
- `ml2_conf.ini` 에 type_drivers 로 sangwooktype, mechanism_drivers 로 sangwookmech 를 지정하면 된다.

## 결과

`neutron-server` 를 시작하면 `__init__` 함수에 추가한 로그가 아래와 같이 출력된다.

```
2015-04-03 02:06:59.091 48 INFO sangwook.type_sangwook [-] sangwooklogtest: __init__
2015-04-03 02:06:59.094 48 INFO sangwook.mech_sangwook [-] sangwooklogtest: __init__
```

sangwooktype, sangwookmech 관련 로그 전체:

```
2015-04-03 02:06:59.090 48 INFO neutron.plugins.ml2.managers [-] Configured type driver names: ['sangwooktype']
2015-04-03 02:06:59.090 48 DEBUG stevedore.extension [-] found extension EntryPoint.parse('sangwooktype = sangwook.type_sangwook:SangwookTypeDriver') _load_plugins /usr/lib/python2.7/dist-packages/stevedore/extension.py:156
2015-04-03 02:06:59.091 48 INFO sangwook.type_sangwook [-] sangwooklogtest: __init__
2015-04-03 02:06:59.092 48 INFO neutron.plugins.ml2.managers [-] Loaded type driver names: ['sangwooktype']
2015-04-03 02:06:59.092 48 INFO neutron.plugins.ml2.managers [-] Registered types: ['sangwooktype']
2015-04-03 02:06:59.092 48 INFO neutron.plugins.ml2.managers [-] Tenant network_types: ['sangwooktype']
2015-04-03 02:06:59.094 48 INFO neutron.plugins.ml2.managers [-] Configured mechanism driver names: ['sangwookmech']
2015-04-03 02:06:59.094 48 DEBUG stevedore.extension [-] found extension EntryPoint.parse('sangwookmech = sangwook.mech_sangwook:SangwookMechanismDriver') _load_plugins /usr/lib/python2.7/dist-packages/stevedore/extension.py:156
2015-04-03 02:06:59.094 48 INFO sangwook.mech_sangwook [-] sangwooklogtest: __init__
2015-04-03 02:06:59.097 48 INFO neutron.plugins.ml2.managers [-] Loaded mechanism driver names: ['sangwookmech']
2015-04-03 02:06:59.097 48 INFO neutron.plugins.ml2.managers [-] Registered mechanism drivers: ['sangwookmech']
2015-04-03 02:06:59.200 48 INFO neutron.plugins.ml2.managers [-] Initializing driver for type 'sangwooktype'
2015-04-03 02:06:59.200 48 INFO neutron.plugins.ml2.managers [-] Initializing mechanism driver 'sangwookmech'
2015-04-03 02:06:59.346 48 DEBUG neutron.service [-] ml2.mechanism_drivers          = ['sangwookmech'] log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2000
2015-04-03 02:06:59.346 48 DEBUG neutron.service [-] ml2.tenant_network_types       = ['sangwooktype'] log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2000
2015-04-03 02:06:59.347 48 DEBUG neutron.service [-] ml2.type_drivers               = ['sangwooktype'] log_opt_values /usr/lib/python2.7/dist-packages/oslo/config/cfg.py:2000
```
