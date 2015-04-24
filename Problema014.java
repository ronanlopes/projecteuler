public class Problema014{
	public static final int limit=1000000;
	
	public static void main (String args[]){
		int maiorSeq=0;
		int maiorTermo=0;
		int tamSeq;
		long termo;
		for (int i=2; i<=limit;i++){
			tamSeq=0;
			termo = i;
			while (termo>1){
				if (termo%2==0){
					termo=even(termo);
				}else{
					termo=odd(termo);
				}
				tamSeq++;
			}
			if (tamSeq>maiorSeq){
				maiorSeq=tamSeq;
				maiorTermo=i;
			}
		}
		System.out.println("Maior Sequência: "+maiorTermo);
	}

	public static long even(long x){
		return x/2;
	}

	public static long odd (long x){
		return 3*x+1;
	}
}
