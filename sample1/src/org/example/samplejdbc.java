package org.example;

import java.rmi.*;

public interface samplejdbc extends Remote {
    public void update( String username, String password) throws RemoteException;
    public void delete( String username) throws RemoteException;
    public void create( String username, String password) throws RemoteException;
    public void read( ) throws RemoteException;
}
