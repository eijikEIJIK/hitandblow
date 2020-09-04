import time
import random

'''
数当てゲームをn回戦行い、合計の所要時間、ラップタイム、スプリットを記録し
ます。
ゲーム数を入力すると時間の計測を開始し、数字を当てるとラップタイム、
ストリップが記録されます。
0を入力するとその時点で計測終了となります。

ルール：各桁の数がそれぞれ異なる4桁の数を当てるゲームです。
各桁は0~9のいずれかで構成されています。
4桁の数を入力すると、"場所まで合っている数字の数(Hit)"、
"場所は合っていないが答えに含まれている数字の数(Blow)"が
ヒントとして与えられます。
その情報を基に答えとなる4桁の数字を当てます。
'''

#各桁がそれぞれ0~9のいずれかで構成され、かつそれぞれが異なる4桁の数を生成する
def generate_answer():
  ans=[]
  count=0
  while count<4:
    a=str(random.randint(0,9))
    judgement=True
    if count>0:
      for i in ans:
        if a==i:
          judgement=False
          break
    if judgement==False:
      continue
    else:
      ans.append(str(a))
      count+=1
  return ans

#計測
class Meas:
  def start(self): #開始時間を取得
    self.now=time.time()
    self.last=self.now
    return self.now
  def stop(self): #所要時間を取得
    stop=time.time()-self.now
    return stop
  def raptime(self): #ラップタイムを取得
    a=time.time()
    raptime=a-self.last
    self.last=a
    return raptime
  def split(self): #スプリットを取得
    a=time.time()
    split=a-self.now
    return split

#ゲーム開始
meas=Meas()

print('数当てゲームをします。各桁の数がそれぞれ異なる4桁の数を当ててください。各桁は0~9のいずれかです。\n')
n=int(input('何回戦行いますか？:'))
meas.start()  #計測開始
print('計測開始\n計測を終了する場合は 0 を入力してください')
end=False     #計測を中断した場合Trueを代入
rapli=[]      #ラップタイムを格納
splitli=[]    #スプリットを格納

for k in range(n):
  ans=generate_answer() #答えを生成
  #print(ans)
  while True: #当たるまでループ
    pred=list(input('各桁の数がそれぞれ異なる4桁の数を入力してください：')) 
    if len(pred)==1 and pred[0]=='0': #計測終了処理
      stop=meas.stop() #合計時間取得
      print('\n計測を終了します。')
      end=True
      break  
      
    #場所まで一致している数の個数を数える
    hit=0
    for i in range(4):
      if ans[i]==pred[i]:
        hit+=1
    #場所はあっていないが含まれている数の個数を数える
    blow=0
    for i in range(4):
      for j in range(4):
        if i==j:
          continue
        if ans[i]==pred[j]:
          blow+=1
    
    if hit==4: #正解だった場合
      raptime=meas.raptime() #raptime取得
      split=meas.split()  #split取得
      rapli.append(raptime)
      splitli.append(split)
      if k==n-1:
        stop=meas.stop() #合計時間取得
      break
    else: #不正解だった場合
      print('Hit ：'+str(hit)+'\nBlow：'+str(blow))
    
  if end==False: #中断していない場合
    print('正解です。答えは'+ans[0]+ans[1]+ans[2]+ans[3]+'でした。')
    print('ラップタイム：'+'{:.3f}'.format(raptime)+'s')
    print('スプリット：'+'{:.3f}'.format(split)+'s')
  else: #中断した場合
    break

print('\n結果')
count=1
for i,j in zip(rapli,splitli):
  print(str(count)+'  ラップタイム:'+'{:.3f}'.format(i)+'s,  スプリット:'+'{:.3f}'.format(j)+'s')
  count+=1
print('合計時間:'+'{:.3f}'.format(stop)+'s')
