import pickle

#------------------------------------------------------
mode = (4202, 4112, 'REG_1x1_4202x4112+0+0', 'B3000', 'R7000', 'RT560', '[1:4202,1:4112]', '[1:4202,1:4112]', '1 1', '[1:4202,1:4112]', '[1:4202,1:4112]', '[1:4202,1:4112]')

#------------------------------------------------------
bias_obs = [
   'T2m3wb-20190905.082316-0002', 
   'T2m3wb-20190905.082523-0003', 
   'T2m3wb-20190908.071454-0051', 
   'T2m3wb-20190908.071644-0052', 
   'T2m3wb-20190908.071834-0053', 
   'T2m3wb-20190908.072024-0054', 
   'T2m3wb-20190908.072214-0055', 
   'T2m3wb-20190908.073051-0057', 
   'T2m3wb-20190908.073242-0058', 
   'T2m3wb-20190908.073432-0059', 
   'T2m3wb-20190908.073622-0060', 
    ]

domeflat_obs = [
   'T2m3wb-20190907.075016-0010', 
    ]

twiflat_obs = [
   'T2m3wb-20190907.080627-0013', 
   'T2m3wb-20190907.080402-0012', 
    ]

dark_obs = [
    ]

arc_obs = [
#   'T2m3wb-20190905.084056-0007',
#   'T2m3wb-20190905.114109-0016',
   'T2m3wb-20190906.102512-0001',
#   'T2m3wb-20190906.110157-0002',
#   'T2m3wb-20190906.112407-0003',
#   'T2m3wb-20190906.113728-0004',
#   'T2m3wb-20190907.075252-0011',
   'T2m3wb-20190908.065944-0047', 
   'T2m3wb-20190908.070300-0048', 
    ]

wire_obs = [
   'T2m3wb-20190908.071006-0050', 
   'T2m3wb-20190905.083350-0006', 
   'T2m3wb-20190908.070716-0049', 
   'T2m3wb-20190906.120827-0005', 
   'T2m3wb-20190905.082917-0004', 
   'T2m3wb-20190905.083134-0005', 
    ]

sci_obs = [
    # PA54
#    {'sci'  : ['T2m3wb-20190907.131607-0026'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # PA23
#    {'sci'  : ['T2m3wb-20190907.133337-0027'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # LMC-Miro1b
#    {'sci'  : ['T2m3wb-20190905.184312-0018',
#               'T2m3wb-20190905.190502-0019'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190905.114109-0016',
#               'T2m3wb-20190906.102512-0001']},
    # IC418
    {'sci'  : ['T2m3wb-20190905.190910-0020',
               'T2m3wb-20190907.191018-0046',
               'T2m3wb-20190907.185630-0044',
               'T2m3wb-20190905.180618-0016',
               'T2m3wb-20190907.190323-0045',
               'T2m3wb-20190905.181315-0017'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190908.065944-0047',
#               'T2m3wb-20190906.112407-0003',
#               'T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190906.113728-0004',
               'T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190906.110157-0002'
               ]},
    # Kris-Helix-6
    {'sci'  : ['T2m3wb-20190905.151441-0007'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    # Kris-Helix-2
    {'sci'  : ['T2m3wb-20190905.142734-0005'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    # HD203638
#    {'sci'  : ['T2m3wb-20190905.123854-0019',
#               'T2m3wb-20190905.112100-0011',
#               'T2m3wb-20190905.113301-0014',
#               'T2m3wb-20190905.110308-0009',
#               'T2m3wb-20190905.122830-0018',
#               'T2m3wb-20190905.105733-0008',
#               'T2m3wb-20190905.122523-0017',
#               'T2m3wb-20190905.110820-0010',
#               'T2m3wb-20190905.112930-0013',
#               'T2m3wb-20190905.124914-0001',
#               'T2m3wb-20190905.112641-0012',
#               'T2m3wb-20190905.113553-0015'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190905.114109-0016',
#               'T2m3wb-20190906.102512-0001']},
    # Kris-Helix12
    {'sci'  : ['T2m3wb-20190907.154355-0034'],
     'sky'  : [],
     'arc'  : [
               'T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190908.065944-0047']},
    # Kris-Helix13
    {'sci'  : ['T2m3wb-20190907.163018-0036',
               'T2m3wb-20190907.160738-0035'],
     'sky'  : [],
     'arc'  : ['T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190908.065944-0047']},
    # Kris-Helix10
    {'sci'  : ['T2m3wb-20190907.145418-0031',
               'T2m3wb-20190907.144222-0030'],
     'sky'  : [],
     'arc'  : ['T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190908.065944-0047']},
    # Kris-Helix-1
    {'sci'  : ['T2m3wb-20190905.161447-0010',
               'T2m3wb-20190905.140253-0004'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    # Kris-Helix11
    {'sci'  : ['T2m3wb-20190907.152053-0033',
               'T2m3wb-20190907.150850-0032'],
     'sky'  : [],
     'arc'  : [
               'T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190908.065944-0047']},
    # Kris-Helix-8
    {'sci'  : ['T2m3wb-20190906.141611-0008'],
     'sky'  : [],
     'arc'  : ['T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190907.075252-0011'
               ]},
    # MPA1751-3128
#    {'sci'  : ['T2m3wb-20190907.095252-0018'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1729-3513
#    {'sci'  : ['T2m3wb-20190907.104332-0019'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # LMC-Miro-1
#    {'sci'  : ['T2m3wb-20190905.172457-0013',
#               'T2m3wb-20190905.170307-0012',
#               'T2m3wb-20190905.164117-0011'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190905.114109-0016',
#               'T2m3wb-20190906.102512-0001']},
    # LMC-0549-6941SNR
#    {'sci'  : ['T2m3wb-20190907.174452-0039',
#               'T2m3wb-20190907.172118-0038',
#               'T2m3wb-20190907.180642-0040'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # PHR1726-2326
#    {'sci'  : ['T2m3wb-20190907.111249-0020'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # FP1804-2105
#    {'sci'  : ['T2m3wb-20190908.124553-0063'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190908.070300-0048']},
    # LMC-Miro-sky
#    {'sci'  : ['T2m3wb-20190905.173751-0014'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190905.114109-0016',
#               'T2m3wb-20190906.102512-0001']},
    # MPQ1854-1420
#    {'sci'  : ['T2m3wb-20190905.131858-0002',
#               'T2m3wb-20190905.132921-0003'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190905.114109-0016',
#               'T2m3wb-20190906.102512-0001']},
    # HaWe14
#    {'sci'  : ['T2m3wb-20190907.135526-0029'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1907-1043
#    {'sci'  : ['T2m3wb-20190906.132238-0006'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190906.113728-0004',
#               'T2m3wb-20190907.075252-0011']},
    # HD157457
#    {'sci'  : ['T2m3wb-20190907.084715-0015',
#               'T2m3wb-20190907.084923-0016',
#               'T2m3wb-20190907.084334-0014'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # IPHAS193305.9+132921
#    {'sci'  : ['T2m3wb-20190907.125716-0025'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1909-0242
#    {'sci'  : ['T2m3wb-20190906.134247-0007'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190906.113728-0004',
#               'T2m3wb-20190907.075252-0011']},
    # Kris-Helix-sky
    {'sci'  : ['T2m3wb-20190905.152839-0008'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    # Kris-Helix7-Sky
    {'sci'  : ['T2m3wb-20190907.165244-0037'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190906.102512-0001',
               'T2m3wb-20190908.065944-0047']},
    # HD176047
#    {'sci'  : ['T2m3wb-20190908.085412-0061'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190908.070300-0048']},
    # Kris-Helix-4
    {'sci'  : ['T2m3wb-20190905.145053-0006'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    # MPA1654-4041
#    {'sci'  : ['T2m3wb-20190908.092054-0062'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190908.070300-0048']},
    # We4-5
#    {'sci'  : ['T2m3wb-20190907.123920-0024'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1827-1328
#    {'sci'  : ['T2m3wb-20190907.115539-0022'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1854-1420
#    {'sci'  : ['T2m3wb-20190907.122129-0023'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # Pa13
#    {'sci'  : ['T2m3wb-20190907.134609-0028'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # MPA1759-3007
#    {'sci'  : ['T2m3wb-20190907.114218-0021'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # LMC0549-6941-offsetsky
#    {'sci'  : ['T2m3wb-20190907.183008-0041'],
#     'sky'  : [],
#     'arc'  : ['T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190908.065944-0047']},
    # Kris-Helix-9
    {'sci'  : ['T2m3wb-20190906.144835-0009'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190906.113728-0004',
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190906.102512-0001'
               ]},
    # Kris-Helix-3
    {'sci'  : ['T2m3wb-20190905.155138-0009'],
     'sky'  : [],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190906.102512-0001']},
    ]

std_obs = [    # LTT1020
    {'sci'  : ['T2m3wb-20190907.184726-0043',
               'T2m3wb-20190907.183952-0042',
               'T2m3wb-20190905.175142-0015'],
     'name' : ['LTT1020'],
     'type' : ['flux', 'telluric'],
     'arc'  : [
#               'T2m3wb-20190905.114109-0016',
               'T2m3wb-20190908.065944-0047',
#               'T2m3wb-20190906.112407-0003',
#               'T2m3wb-20190907.075252-0011',
#               'T2m3wb-20190906.113728-0004',
               'T2m3wb-20190906.102512-0001',
#               'T2m3wb-20190906.110157-0002'
               ]},
    # LTT7379
    {'sci'  : ['T2m3wb-20190907.090249-0017'],
     'name' : ['LTT7379'],
     'type' : ['flux', 'telluric'],
     'arc'  : [
#               'T2m3wb-20190907.075252-0011',
               'T2m3wb-20190908.065944-0047']},
    ]

#------------------------------------------------------
night_data = {
    'bias' : bias_obs,
    'domeflat' : domeflat_obs,
    'twiflat' : twiflat_obs,
#    'dark' : dark_obs,
    'wire' : wire_obs,
    'arc'  : arc_obs,
    'sci'  : sci_obs,
    'std'  : std_obs}

f1 = open('wifesB_0919_metadata.pkl', 'wb')
pickle.dump(night_data, f1)
f1.close()
