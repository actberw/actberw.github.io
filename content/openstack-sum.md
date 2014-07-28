Title: openstack
1. openstack简介  
  OpenStack是一个由rackspace和NSNA于2010年发布的云计算平台, 旨在为公有云和私有云提供一个易于扩展的、功能丰富的解决方案，也可以说OpenStack是一个云计算操作系统，它整合各种底层硬件硬件资源，为系统管理员提供Web界面的控制面板以方便资源管理，为开发者的应用程序提供统一管理接口，为终端用户提供无缝的透明的云计算服务。最近的icehouse版本主要包含了10个核心组件：  
    - 计算(Nova)
    - 对象存储(Swift)
    - 块存储(Cinder)
    - 镜像(Glance)
    - 网络(Neutron)
    - 身份认证(Keystone)
    - 控制面板(Horizon)
    - 计量/监控服务(Ceilometer)
    - 编排组织服务(Heat)
    - 数据库服务(Trove)。

2. openstack部署  
    - 部署模型一般是Three-node architecture, 分别是:  
        - 控制节点
        - 网络节点
        - 计算机点

    - 潜在的技术难点   
        - 网络  
        虚拟机比较多的情况下，虚拟网络会更加复杂, CPU需要消耗大量的资源匹配网络流表，灵活的网络管理会境地网络的性能。
        - 镜像风暴  
        当镜像较多且每个镜像都很大时会消耗更多的网络宽带和 IO。
        - openstack api  
        每个openstack组件的api都监听单一端口，导致无法充分利用服务器资源，原生的dashboard使用同步方式调用api会导致用户端界面变慢
        - 资源调度  
        内置的默认资源调度可能无法满足复杂的业务需求
        - 异构存储  
        企业内部异构存储新旧不一, 架构不一需要整合

    - 网络设计  
    Neutron 实质是一个定义良好的框架用来驱动 L2-L7 层不同的底层网络技术来为第三方应用独立地提供租户隔离的虚拟网络服务。目前支持的有flat, flatdhcp, vlan, vxlan, nvgre, mpls, openflow等。
