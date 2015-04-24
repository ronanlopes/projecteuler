import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;

public class Problema013{

	public static void main (String args[]){
		try{
			FileReader entrada = new FileReader("in/013.txt");
			BufferedReader reader = new BufferedReader(entrada);
			BigInteger bi = BigInteger.ZERO;
			String linha;
			while ((linha=reader.readLine())!=null){
				BigInteger big = new BigInteger(linha);
				bi = bi.add(big);
			}
			System.out.println("Resultado da soma:"+bi.toString().substring(0,10));
		}catch (FileNotFoundException notfound){
			System.out.println(notfound.getMessage());
		}catch (IOException io){
			System.out.println(io.getMessage());
		}
	}

}
