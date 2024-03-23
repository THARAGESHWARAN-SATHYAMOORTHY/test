package org.example;
import java.net.MalformedURLException;
import java.rmi.*;

import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try{
            System.setProperty("java.rmi.server.hostname","10.1.67.137");
            LocateRegistry.createRegistry(10000);
            samplejdbc a =new database();
            Naming.bind("rmi://10.1.67.137:10000/data",a);
        }catch(Exception a)
        {}
    }

}
