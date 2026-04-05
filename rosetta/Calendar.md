+++
title = "Calendar"
+++

# Calendar

```zc
fn IS_LEAP(Y: int) -> int {
    if Y > 1582 return (Y % 4 == 0 && Y % 100 != 0) || (Y % 400 == 0) ? 1 : 0;
    return Y % 4 == 0 ? 1 : 0;
}

fn GET_DAYS(Y: int, M: int) -> int {
    if M == 2 return IS_LEAP(Y) == 1 ? 29 : 28;
    if M == 4 || M == 6 || M == 9 || M == 11 return 30;
    return 31;
}

fn GET_START_DAY(Y: int, M: int) -> int {
    let TY = Y;
    let TM = M;
    if TM < 3 { TY--; TM += 12; }
    if Y > 1582 || (Y == 1582 && M > 10) {
        return (1 + 2*TM + 3*(TM+1)/5 + TY + TY/4 - TY/100 + TY/400 + 1) % 7;
    }
    return (1 + 2*TM + 3*(TM+1)/5 + TY + TY/4 + 5) % 7;
}

fn PRINT_MONTH_NAME(M: int) {
    let NAMES: char*[12] = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"];
    let NAME = NAMES[M-1];
    print "      {NAME}";
    // Simple padding for 20-char width
    for I in 0..(14 - (M == 9 ? 9 : (M == 1 || M == 3 || M == 7 || M == 8 ? 7 : 8))) { print " "; }
}

fn main() {
    let YEAR = 1969;
    let WIDTH = 80;
    let MONTHS_PER_ROW = WIDTH / 20;

    println "                                    ,-~~-.___.";
    println "                                   / ()=(()   \\";
    println "                                  (   (        0";
    println "                                   \\._\\, ,----'";
    println "                              ##XXXxxxxxxx";
    println "                                     /  ---'~;";
    println "                                    /    /~|-";
    println "                              _____=(   ~~  |______";
    println "                             /_____________________\\";
    println "                            /_______________________\\";
    println "                           /_________________________\\";
    println "                          /___________________________\\";
    println "                             |____________________|";
    println "                             |____________________|";
    println "                             |____________________|";
    println "                               CALENDAR FOR {YEAR}";

    for ROW in 0..(12 / MONTHS_PER_ROW) {
        let START_M = ROW * MONTHS_PER_ROW + 1;
        
        // Headers
        for M_OFF in 0..MONTHS_PER_ROW { PRINT_MONTH_NAME(START_M + M_OFF); }
        println "";
        for M_OFF in 0..MONTHS_PER_ROW { print "SU MO TU WE TH FR SA "; }
        println "";

        // Weeks (Max 6)
        for W in 0..6 {
            for M_OFF in 0..MONTHS_PER_ROW {
                let M = START_M + M_OFF;
                let S = GET_START_DAY(YEAR, M);
                let D_MAX = GET_DAYS(YEAR, M);
                for D in 0..7 {
                    let DATE = W * 7 + D - S + 1;
                    if DATE > 0 && DATE <= D_MAX {
                        if DATE < 10 print " ";
                        print "{DATE} ";
                    } else {
                        print "   ";
                    }
                }
            }
            println "";
        }
    }
}
```

**Output:**

```
,-~~-.___.
                                   / ()=(()   \
                                  (   (        0
                                   \._\, ,----'
                              ##XXXxxxxxxx
                                     /  ---'~;
                                    /    /~|-
                             _____=(   ~~  |______
                            /_____________________\
                           /_______________________\
                          /_________________________\
                         /___________________________\
                            |____________________|
                            |____________________|
                            |____________________|
                              CALENDAR FOR 1969
      JANUARY             FEBRUARY            MARCH             APRIL      
SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA 
          1  2  3  4                    1                    1        1  2  3  4  5 
 5  6  7  8  9 10 11  2  3  4  5  6  7  8  2  3  4  5  6  7  8  6  7  8  9 10 11 12 
12 13 14 15 16 17 18  9 10 11 12 13 14 15  9 10 11 12 13 14 15 13 14 15 16 17 18 19 
19 20 21 22 23 24 25 16 17 18 19 20 21 22 16 17 18 19 20 21 22 20 21 22 23 24 25 26 
26 27 28 29 30 31    23 24 25 26 27 28    23 24 25 26 27 28 29 27 28 29 30          
                                          30 31                                     
      MAY            JUNE            JULY             AUGUST       
SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA 
             1  2  3  1  2  3  4  5  6  7        1  2  3  4  5                 1  2 
 4  5  6  7  8  9 10  8  9 10 11 12 13 14  6  7  8  9 10 11 12  3  4  5  6  7  8  9 
11 12 13 14 15 16 17 15 16 17 18 19 20 21 13 14 15 16 17 18 19 10 11 12 13 14 15 16 
18 19 20 21 22 23 24 22 23 24 25 26 27 28 20 21 22 23 24 25 26 17 18 19 20 21 22 23 
25 26 27 28 29 30 31 29 30                27 28 29 30 31       24 25 26 27 28 29 30 
                                                               31                   
      SEPTEMBER           OCTOBER            NOVEMBER            DECEMBER      
SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA SU MO TU WE TH FR SA 
    1  2  3  4  5  6           1  2  3  4                    1     1  2  3  4  5  6 
 7  8  9 10 11 12 13  5  6  7  8  9 10 11  2  3  4  5  6  7  8  7  8  9 10 11 12 13 
14 15 16 17 18 19 20 12 13 14 15 16 17 18  9 10 11 12 13 14 15 14 15 16 17 18 19 20 
21 22 23 24 25 26 27 19 20 21 22 23 24 25 16 17 18 19 20 21 22 21 22 23 24 25 26 27 
28 29 30             26 27 28 29 30 31    23 24 25 26 27 28 29 28 29 30 31          
                                          30
```

---
**Attribution:** This is a community solution for the Rosetta Code task [**Calendar**](https://rosettacode.org/wiki/Calendar) in Zen C.

*This article uses material from the Rosetta Code article **Calendar**, which is released under the [GNU Free Documentation License 1.3](https://www.gnu.org/licenses/fdl-1.3.html). A list of the original authors can be found in the [page history](https://rosettacode.org/wiki/Calendar?action=history).*
