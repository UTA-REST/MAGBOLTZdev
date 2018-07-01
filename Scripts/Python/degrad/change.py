'''This is a Python 3 script '''
# AUTHOR : Mayank Modi        #
#          fireballpoint1     #
import string
map_list=[('!','#'),
    ('\t','    '),
    ('.d0','.0'),
    ('d0','0'),
    ('.eq.',' == '),
    ('.ne.',' != '),
    ('/=',' != '),
    ('.lt.',' < '),
    ('.gt.',' > '),
    ('.le.',' <= '),
    ('.ge.',' >= '),
    ('then',':'),
    ('else if','elif'),
    ('else','else:'),
    ('&','\\'),
    ('.and.',' and '),
    ('.or.',' or '),
    ('.true.',' True '),
    ('.false.',' False '),
    ('end if',''),
    ('do while','while'),
    ('end do',''),
    ('end program','# end program'),
    ('end function','# end function'),
    ('end subroutine','# end subroutine'),
    ('end','# end'),
    ('program','def'),
    ('function','def'),
    ('subroutine','def'),
    ('integer','#integer'),
    ('real','#real'),
    ('allocate','#allocate'),
    ('IF','if'),
    ('FORMAT','print')
    ]
map_list_v2=[
('IF','if'),
('DFLOAT','float'),
('STOP','sys.exit()'),
('RETURN','return'),
]

map_list_gas=[
('(1)','[1]'),
('(2)','[2]'),
('(3)','[3]'),
('(4)','[4]'),
('(5)','[5]'),
('(6)','[6]'),
('(7)','[7]'),
('(8)','[8]'),
('(9)','[9]'),
('(10)','[10]'),
('(11)','[11]'),
('(12)','[12]'),
('(13)','[13]'),
('(14)','[14]'),
('(15)','[15]'),
('(16)','[16]'),
('(17)','[17]'),
('(18)','[18]'),
('(19)','[19]'),
('(20)','[20]'),
('(21)','[21]'),
('(22)','[22]'),
('(23)','[23]'),
('(24)','[24]'),
('(25)','[25]'),
('(26)','[26]'),
('(27)','[27]'),
('(28)','[28]'),
('(29)','[29]'),
('(30)','[30]'),
('(31)','[31]'),
('(32)','[32]'),
('(33)','[33]'),
('(34)','[34]'),
('(35)','[35]'),
('(36)','[36]'),
('(37)','[37]'),
('(38)','[38]'),
('(39)','[39]'),
('(40)','[40]'),
('(41)','[41]'),
('(42)','[42]'),
('(43)','[43]'),
('(44)','[44]'),
('(45)','[45]'),
('(46)','[46]'),
('(47)','[47]'),
('(48)','[48]'),
('(49)','[49]'),
('(50)','[50]'),
('(51)','[51]'),
('(52)','[52]'),
('(53)','[53]'),
('(54)','[54]'),
('(55)','[55]'),
('(56)','[56]'),
('(57)','[57]'),
('(58)','[58]'),
('(59)','[59]'),
('(60)','[60]'),
('(61)','[61]'),
('(62)','[62]'),
('(63)','[63]'),
('(64)','[64]'),
]
math_list=[
    ('dabs','abs'),
    ('dsqrt','math.sqrt'),
    ('dlog','math.log'),
    ('dexp','math.exp'),
    ('dacos','numpy.arccos'),
    ('drand48','random.uniform'),
    ('dsin','numpy.sin'),
    ('dcos','numpy.cos'),
    ('dasin','numpy.arcsin'),
    ('dint','int'),
    ]


def file2list(fname, include_eol=False):
    ''' text file to list of string '''
    with open(fname, encoding="utf8") as f:
        if include_eol:
            content = f.readlines() # \n is included
        else:
            content = f.read().splitlines() # \n is not included
        return content

def ireplace(old, new, text):
    ''' Case Insensitive Replace excluding comments
    based on
    http://stackoverflow.com/questions/919056/python-case-insensitive-replace
    ''' 
    idx = 0
    lim = text.find('#')
    if lim < 0:
        lim = len(text)
    while idx < lim:
#     while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(old)
    return text
def replace_statements(content,map_list):
    ''' replaice all statements in map_list for all lines '''
    result = list(content) # make a copy
    for p in map_list:
#         result = [l.replace(p[0], p[1]) for l in result] # Case-sensitive
        result = [ireplace(p[0], p[1], l) for l in result]
    return result
def replace_math_functions(content,math_list):
    ''' replace all math functions in content '''
    for p in math_list:
        content = [ireplace(p[0], p[1], l) for l in content]
    return content

def process_do(line):
    ''' replaice Fortran do to Python for:
        do i=1, N => for i in range(0, N):
        do j=1, M, 2 => for j in range(0, M, 2):
        do iq=ip+1, N => for iq in range(ip+1, N):
    '''
    if line.startswith('C'):
        return line
    if line.strip().startswith( 'do' ) and line.strip().startswith('double')!=1:
        if '#' in line:
            do_var_lims,comment = line.split('#')
            comment = ' #'+''.join(comment)
        else:
            do_var_lims,comment = line,''
        do_var,lims = do_var_lims.split('=')
        for_var = do_var.replace('do','for') + ' in range('
        lims=lims.split(',')
        lims=[i.strip() for i in lims]
        if str(lims[0])=='1':     # heuristic correction for 0-based arrays    
            lims[0]='0'           # warning: this can be unnecessery sometimes.
        result = for_var + ', '.join(lims) + '):'
        if comment:
            result += comment
        return result
    else:
        return line
def replace_all_do(content):
    ''' replaice do statements for all lines '''
    result = [process_do(l) for l in content]
    return result
def adjust_array(line, arr):
    ''' Conversion of Fortran array access to Python:
        line = 'A(i,j) = A(m,A(k,l))'
        arr = 'A'
        result = 'A[i,j] = A[m,A[k,l]]'
    '''
    if line.startswith('C'):
        return line.replace("C",'#',1)
    i = line.find(arr+'(')
    while i >= 0:
        j = line.find('(',i)
        line = line[:j] + '[' + line[j+1:]
        c = 1
        for k in range(j+1,len(line)):
            if line[k] == '(':
                c += 1
            if line[k] == ')':
                c -= 1
            if c == 0:
                line = line[:k] + ']' + line[k+1:]
#                 i = line.find(arr+'(', k+1) # does not process nested arrays
                i = line.find(arr+'(')
                break
    return line
def adjust_arrays(line):
    ''' adjust all arrays in a line '''
    for a in arrays:
        line = adjust_array(line, a)
    return line

def adjust_all_arrays(content):
    ''' adjust all arrays in all lines '''
    result = [adjust_arrays(l) for l in content]
    return result

def adjust_functions(content):
    """ Adds ':' after ')' """    
    for n,line in enumerate(content):
        count = 0
        if line.strip().startswith('def'):
            i = line.find('(')
            if i >= 0:
                count = 1
                for k in range(i,len(line)):
                    #print(k, line[k])
                    if line[k] == '#':
                        break
                    if line[k] == ')':
                        count = 0
                        content[n] = line[:k+1] + ':' + line[k+1:]
                        break
            else:
                count = 0
                i = line.find('#') 
                if i >= 0:
                    content[n] =  line[:i] + ':' + line[i:]
                else:
                    content[n] =  line + ':'
        else:
            if count > 0:
                i = 0
                for k in range(i,len(line)):
                    if line[k] == '#':
                        break
                    if line[k] == ')':
                        count = 0
                        content[n] = line[:k+1] + ':' + line[k+1:]
                        break
    return content
def make_arrays(content):
    for n,line in enumerate(content):
        count=0
        if line.strip().startswith('DATA'):
            i=line.find('/')
            # print(i,line)
            # print(line[i])
            if i>0:
                # content[n]=str(line)
                # print(content[n])
                for k in range(i,len(line)+1):
                    if(line[k]=='#'):
                        break
                    if line[k]=='/':
                        if count==0:
                            content[n]=line[:k]+'=['+line[k+1:]
                            # print(content[n])
                            count=count+1
                        elif count==1 and len(line)>k:
                            content[n]=line[:k]+']'+line[k+1:]
                            # print(content[n])
                            count=count-1
                        elif count==1 and len(line)==k:
                            content[n]=line[:k]+']'
                            # print(content[n])
                            count=count-1
                        line=content[n]
                print(content[n])
    return content

def adjust_ifs(content):
    """ Adds ':' after ')' """    
    for n,line in enumerate(content):
        count = 0
        if line.strip().startswith('IF'):
            i = line.find('(')
            if i >= 0:
                count = 1
                for k in range(i,len(line)):
                    #print(k, line[k])
                    if line[k] == '#':
                        break
                    if line[k] == ')':
                        count = 0
                        if k==len(line)-1 :
                            content[n] = line[:k+1] + ':' + line[k+1:]
                        elif line[k+1] != ':':
                            content[n] = line[:k+1] + ':\n' + line[k+1:]
                        break
            else:
                count = 0
                i = line.find('#') 
                if i >= 0:
                    content[n] =  line[:i] + ':' + line[i:]
                else:
                    content[n] =  line + ':'
        else:
            if count > 0:
                i = 0
                for k in range(i,len(line)):
                    if line[k] == '#':
                        break
                    if line[k] == ')':
                        count = 0
                        content[n] = line[:k+1] + ':' + line[k+1:]
                        break
    return content

def list2file(fname, output):
    ''' list of string to text file '''
    with open(fname,'w', encoding="utf8") as out:
        for line in output:
            out.write(line+'\n')

def f_to_py(content,map_list,math_list,arrays):
    ''' Fortran 90 to Python conversion 
        by string manipulations
        content - input list of f90 file content strings
        map_list - list of substitution pairs, 
                   e.g. ('.lt.',' < '),('DABS','abs'),
        output - list of python file content strings
    '''
    #output = replace_statements(content,map_list)
    #output = replace_math_functions(output,math_list)
    output = make_arrays(content)
    print("remember to check all float statements for square braces in degrad  ")
#    output = replace_all_do(output)
#    output = adjust_all_arrays(output)
#    output = adjust_functions(output)
#    output = adjust_ifs(output)
    return output

fname='Gasn.py'
foutname='Gasn1.py'
arrays=['A','D','V','B','Z']
content = file2list(fname)
output = f_to_py(content,map_list_gas,math_list,arrays)
list2file(foutname, output)

