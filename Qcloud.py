import qingcloud.iaas

conn = qingcloud.iaas.connect_to_zone(
        'pek3a', # 你的资源所在的节点ID，可在控制台切换节点的地方查看，如 'pek1', 'pek2', 'gd1' 等
        'JTKQUECFLOCIORFAJKXJ',
        '3L5Zt3C9lrlaouDT89FaGvag33p6vfiL7UcN0eUg'
    )

def showall():
    ret = conn.describe_instances(limit=50)
    all_instances = ret['instance_set']
    return all_instances
def showrun():
    ret = conn.describe_instances(status=['running'])
    running_instances = ret['instance_set']
    return running_instances
def showtest():
    ret = conn.describe_instances(search_word='test')
    test_instances = ret['instance_set']
    return test_instances
def stophost(hostname):
    ret = conn.stop_instances(
        instances=[hostname]
    )
print(showall())
print(showrun())

