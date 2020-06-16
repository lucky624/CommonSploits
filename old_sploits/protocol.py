from swpag_client import Team



t = Team("http://teaminterface.ictf.love/", "W7PMqeQCuYjVeL03UnV3")

flags = ['FLGxxxxxxxxxxxxx']


print(t.submit_flag(flags))