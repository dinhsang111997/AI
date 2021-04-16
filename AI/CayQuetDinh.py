from sklearn import tree
#CAC BUOC THUC HIEN
#Buoc1:Thu thap du lieu
#Buoc2:Xu ly du lieu
#Buoc3:Xay dung model
#Buoc4:Du doan ket qua
#Buoc5:Danh gia xem model co hieu qua hay khong
mytree=tree.DecisionTreeClassifier()
dactrung=[[1,3,3,7],
          [5,2,4,6],
          [5,2,4,6],
          [5,4,4,3],
          [1,4,4,7],
          [3,2,3,7],
          [3,3,3,6],
          [5,2,2,7]
          ]
nhan=[0,1,1,0,0,0,0,1]
resul=mytree.fit(dactrung,nhan)
kq=resul.predict([[1,3,4,6],[5,2,4,6]])
print(kq)