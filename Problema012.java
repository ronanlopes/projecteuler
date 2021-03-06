public class Problema012{
	public static void main (String args[]){
		int i=1;
		int triangular=i*(i+1)/2; //Calculando o iésimo triangular
		while (numeroDivisores(triangular)<=500){
			i++;
			triangular=i*(i+1)/2;
		}
		System.out.println("Triangular com 500+ divisores: "+triangular);
	}
	

	public static int numeroDivisores(int x){
		int n=0;
		int raiz = (int) Math.sqrt(x);
		for (int i=1;i<=raiz;i++){
			if (x%i==0) n+=2;
		}
		if (raiz*raiz==x) n--;	//Remover uma das contagens, caso igual (exemplo 25, onde 5x5=25)
		return n;
	}
}
