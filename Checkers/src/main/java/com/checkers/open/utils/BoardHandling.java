package com.checkers.open.utils;

import com.checkers.open.enumeration.GamePlayer;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.logging.Level;
import java.util.logging.Logger;

//testing class
public abstract class BoardHandling {

    public static void writeErrors(String message) {
        try {
            PrintWriter writer = new PrintWriter("error.txt");
            writer.write(message);
            writer.close();
        } catch (FileNotFoundException ex) {
            Logger.getLogger(BoardHandling.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public static boolean acceptClick(String gamePlayerFlag) {
        return gamePlayerFlag.equals(GamePlayer.HUMAN.getPlayerFlag()) || gamePlayerFlag.equals(GamePlayer.HUMANKING.getPlayerFlag());
    }
}
