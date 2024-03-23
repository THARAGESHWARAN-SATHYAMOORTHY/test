package org.example;

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        Map<String, Integer> dictionary = new HashMap<>();

        dictionary.put("Apple", 10);
        dictionary.put("Banana", 5);
        dictionary.put("Orange", 8);
        dictionary.put("Grapes", 15);

        for(Map.Entry<String, Integer> entry : dictionary.entrySet()){
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }

        ArrayList<String> keys = new ArrayList<>(dictionary.keySet());
        ArrayList<Integer> list = new ArrayList<>(dictionary.values());
        System.out.println(keys + " : " + list);
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (list.get(j) > list.get(j + 1)) {
                    // Swap list[j] and list[j+1]
                    int temp = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, temp);
                    String temp1 = keys.get(j);
                    keys.set(j, keys.get(j + 1));
                    keys.set(j + 1, temp1);
                }
            }
        }
        System.out.println(keys + " : " +list);


        Integer[] arr = {1, 2, 3, 2, 4, 3, 2, 4, 5};

        Map<Integer, Integer> counter = countOccurrences(arr);

        System.out.println("Element counts:");
        for (Map.Entry<Integer, Integer> entry : counter.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }

    public static <T> Map<T, Integer> countOccurrences(T[] arr) {
        Map<T, Integer> counter = new HashMap<>();

        for (T element : arr) {
            counter.put(element, counter.getOrDefault(element, 0) + 1);
        }

        return counter;
    }
}

