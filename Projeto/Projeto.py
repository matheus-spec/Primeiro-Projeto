np1=0;
np2=0;
mf=0;
ex=0;
ms=0;

np1=float(input("Coloque a nota da sua Prova: "));
np2=float(input("Coloque sua nota do TRABALHO ou Prova: "));

ms=(np1+np2)/2;

if ms < 7:
    print("ESTÁ DE EXAME");

if ms < 7:
    ex=float(input("Digite a nota do exame: "));
    mf=(ms+ex)/2;

if ms >= 7:
    print("Sua media semestral: ",ms);
    print("APROVADO!!");            
elif mf >= 5:
    print("Sua media final: ",mf);
    print("APROVADO!!");
else:
    print("Sua media final: ",mf);
    print("REPROVADO");


        