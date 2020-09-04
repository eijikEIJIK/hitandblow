'''
各桁が0~9のいずれかで構成され、各桁がすべて異なる4桁の整数を当てるプログラムです(先頭が0でもよい)。人が、予測された数字のhitとblowを入力します。hitは、答えと場所も数字も一致している桁の数、blowは、場所は違うが答えに含まれている数字の数を意味します(例：予測が'1357',答えが'1275'ならば、hit=1(先頭の1が正しい),blow=2(5,7が含まれている))。
'''
def Makenumli():#4桁で各位の数がすべて異なる自然数のリストを作成
    li=[]
    for i in range(9999):
      a=list(str(i).zfill(4))
      judge=True
      for j in range(4):
        for k in range(4):
          if j<k:
            if a[j]==a[k]:
              judge=False
      if judge==True:
        li.append(str(i).zfill(4))
    return li

def Judge(li,hit,blow): #候補となる4桁の数のリストとhit,blowを受け取り候補でないものを除外する。
  b=[]
  num=list(li[0])
  for i in li:
    a=list(i)
    #hit
    hitct=0
    for j in range(4):
      if a[j]==num[j]:
        hitct+=1
    #blow
    blowct=0
    for j in range(4):
      for k in range(4):
        if j!=k:
          if a[j]==num[k]:
            blowct+=1
    if hit==hitct and blow==blowct:
      b.append(i)
  if len(b)==0:
    print('入力を誤っている可能性があります。\nやり直してください。')
    return 0
  else:
    return b #答えの可能性がある数のリストを返す

a=Makenumli()
print('あなたが考えた、各桁がすべて異なる4桁の数を当てます。')
count=0
while True:
  print('答えは',a[0],'ですか？') 
  hit=int(input('hit:'))
  blow=int(input('blow:'))
  count+=1
  if hit==4 and blow==0:
    print('答えは',a[0],'ですね。'+str(count)+'回で当てました。')
    break
  else:
    a=Judge(a,hit,blow)
    if a==0:
      break

