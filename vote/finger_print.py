from zk import ZK, const

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5)
try:
    print ('Connecting to device...')
    conn = zk.connect()
    print ('Disabling device ...')
   # zk.enable_device()
    print("print please enroll your finger ")
    #enrol=zk.enroll_user() (uid=5, temp_id=5, user_id='yayal5')

    #print(zk.enroll_user(uid=6, temp_id=6, user_id='6'))
    #print (zk.enroll_user (uid=7, temp_id=7, user_id='7'))
   # conn.disable_device()
   ## print ('--- Get User ---')
   # zk.test_voice (index=4)
    print(zk.verify_user())

    users = conn.get_users()
    print(users)
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'

        print ('- UID #{}').format(user.uid)
        print ('  Name       : {}').format(user.name)
        print ('  Privilege  : {}').format(privilege)
        print ('  Password   : {}').format(user.password)
        print ('  Group ID   : {}').format(user.group_id)
        print ('  User  ID   : {}').format(user.user_id)

    print ("Voice Test ...")
    conn.test_voice()
    print ('Enabling device ...')
    conn.enable_device()
except Exception:
    print ("Process terminate : {}")#.format("erroor")
finally:
    if conn:
        conn.disconnect()