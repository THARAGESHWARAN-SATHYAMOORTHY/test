package org.example;
import java.rmi.Naming;

public class Client {
    public static void main(String[] args){
        try{
            samplejdbc a = (samplejdbc) Naming.lookup("rmi://10.1.67.137:10000/data");
            a.create("abarna","hihello");
            a.read();
            a.update("abarna","12345");
            a.delete("abarna");
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
