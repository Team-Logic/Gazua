# [Gazua] 1차 기획안  



## <목차>  

* [간단 설명](https://github.com/Team-Logic/Gazua/blob/main/Gazua/project_planning/%5BGazua%5D%201%EC%B0%A8%20%EA%B8%B0%ED%9A%8D%EC%95%88.md#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B0%84%EB%8B%A8-%EC%84%A4%EB%AA%85)

* [주식 매도](https://github.com/Team-Logic/Gazua/blob/main/Gazua/project_planning/%5BGazua%5D%201%EC%B0%A8%20%EA%B8%B0%ED%9A%8D%EC%95%88.md#%EC%A3%BC%EC%8B%9D-%EB%A7%A4%EB%8F%84)

* [적정주가](https://github.com/Team-Logic/Gazua/blob/main/Gazua/project_planning/%5BGazua%5D%201%EC%B0%A8%20%EA%B8%B0%ED%9A%8D%EC%95%88.md#%EC%A0%81%EC%A0%95%EC%A3%BC%EA%B0%80)

* [시드머니](https://github.com/Team-Logic/Gazua/blob/main/Gazua/project_planning/%5BGazua%5D%201%EC%B0%A8%20%EA%B8%B0%ED%9A%8D%EC%95%88.md#%EC%8B%9C%EB%93%9C%EB%A8%B8%EB%8B%88)

* [추후에 추가 할 기능들](https://github.com/Team-Logic/Gazua/blob/main/Gazua/project_planning/%5BGazua%5D%201%EC%B0%A8%20%EA%B8%B0%ED%9A%8D%EC%95%88.md#%EC%B6%94%ED%9B%84%EC%97%90-%EC%B6%94%EA%B0%80-%ED%95%A0-%EA%B8%B0%EB%8A%A5%EB%93%A4)  

  



### 프로젝트 간단 설명  

주가의 변동은 초기 기획과는 다르게 __매수와 매도로만 변동되게 제작__ 할 예정이며  
사건으로 인해 기업의 평판이 바뀌면 주가를 변동시키는 것은 아직 보류(개인의 생각에 의해 기업의 평판이 좌우되기 때문)    





### 주식 매도  

현실과 가까운 호가 시스템 도입 예정  

매수호가/매도호가 를 정하고 그 가격에 매수/매도 를 하려는 사람이 나오면 거래가 성사되는 방식  





### 적정주가  

현실에서 표시되는 적정 주가는 매도와 매수가 만나는 지점을 말하며  
__매도잔량과 매수잔량이 만나는 중간지점__ 에서 __매도잔량의 호가__로 결정하는 방법을 택함  

> ex)  
>
> | 매도잔량 | 호가   | 매수잔량 |
> | :------- | ------ | -------- |
> | 148,679  | 72,200 |          |
> |          | 72,100 | 98,120   |
>
> 72,200원에 148679명이 매도를 원함  
> 72,100원에 98120명이 매수를 원함  
>
> -> 다수인 72,200원이 채택됨





### 시드머니  

기초적인 돈을 임의로 지급하거나 현재 전체 종목 주가의 평균 *100 정도임  





### 추후에 추가 할 기능들  

1. *변동성완화장치(VI)*
2. *서킷브레이커*
3. *사이드카*
4. *배당금*  

###### 2021.10.09

​	
