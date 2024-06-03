"""
안밖? 밖안? 계단? 역계단?
"""
S = input()
if S in ['fdsajkl;', 'jkl;fdsa']: print('in-out')
elif S in ['asdf;lkj', ';lkjasdf']: print('out-in')
elif S == 'asdfjkl;': print('stairs')
elif S == ';lkjfdsa': print('reverse')
else: print('molu')