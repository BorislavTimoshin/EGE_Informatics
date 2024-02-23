from re import findall


with open("24_2422.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"A*B*C*D*E*F*G*H*I*J*K*L*M*N*O*P*Q*R*S*T*U*V*W*X*Y*Z*", text)
    print(max(sequences, key=len))
    print(len(max(sequences, key=len)))
