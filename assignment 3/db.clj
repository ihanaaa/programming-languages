(ns db
  (:require [app]))
(def totalvalue 0.00)
(defn loadCTable []
  (def customerst (app/cust))
  (def c1 (count customerst))
  (loop [m 0]
    (when (< m c1)
      (def sep1 (get customerst m))
      (def ins1 (clojure.string/split sep1 #"\|"))
      (println (get ins1 0) ": " (get ins1 1) (get ins1 2) (get ins1 3))
      (recur (+ m 1)))
    ))
(defn loadPTable []
  (def productst (app/prod))
  (def c2 (count productst))
  (loop [n 0]
    (when (< n c2)
      (def sep2 (get productst n))
      (def ins2 (clojure.string/split sep2 #"\|"))
      (println (get ins2 0) ": " (get ins2 1) (get ins2 2))
      (recur (+ n 1)))
    ))
(defn loadSTable []
  (def ct (app/cust))
  (def pt (app/prod))
  (def salest (app/sales))
  (def c3 (count salest))
  (def c4 (count ct))
  (def c5 (count pt))
  (def data [])

  (loop [o 0]
    (when (< o c3)
      (def sep3 (get salest o))
      (def ins3 (clojure.string/split sep3 #"\|"))

      (loop [p 0]
        (def newc (get ins3 1))                             ; value of inside the sales array to know the name
        (when (< p c4)                                      ; to go through all the customers
          (def ctsep (get ct p))                            ; check each individual client
          (def ctins (clojure.string/split ctsep #"\|"))    ; split each client information into its own array

          (def ctinsNum (get ctins 0))                      ; get the first value of the client
          (if (not= (Integer/parseInt newc) (Integer/parseInt ctinsNum))
            (recur (+ p 1))
            (def ctins3 (get ctins 1))
            )))

      (loop [q 0]
        (def newp (get ins3 2))
        (when (< q c5)
          (def ptsep (get pt q))
          (def ptins (clojure.string/split ptsep #"\|"))

          (def ptinsNum (get ptins 0))
          (if (not= (Integer/parseInt newp) (Integer/parseInt ptinsNum))
            (recur (+ q 1))
            (def ptins3 (get ptins 1))
            )
          )
        )

      (println (get ins3 0) ": " ctins3 ptins3 (get ins3 3))
      (recur (+ o 1)))
    )

  )

(defn sales4cust []
  (def custs (app/cust))
  (def prods (app/prod))
  (def sals (app/sales))
  (def ccusts (count custs))
  (def cprods (count prods))
  (def csals (count sals))
  (def cprods (count prods))
  (def totalvalue 0.00)
  (println "Please write the customer's name!")
  (def s (read-line))

  (loop [a 0]
    (when (< a ccusts)
      (def custa (get custs a))                             ; check each individual client
      (def custv (clojure.string/split custa #"\|"))

      (def cname (get custv 1))
      (if (not= s cname)
        (do
          (if (= (+ a 1) ccusts)
            (println "Sorry customer not found!")
            (recur (+ a 1)))
          )
        (do

          (def aaa (+ a 1))
          (loop [b 0]

            (when (< b csals)
              (def salsa (get sals b))
              (def salsv (clojure.string/split salsa #"\|"))
              (def valu (get salsv 1))

              (if (not= aaa (Integer/parseInt valu))
                (do
                  (recur (+ b 1))
                  )
                (do
                  (def itemn (get salsv 2))                 ; from sales.txt
                  (def pricen (get salsv 3))

                  (loop [c 0]
                    (when (< c cprods)
                      (def prodsa (get prods c))
                      (def prodsv (clojure.string/split prodsa #"\|"))
                      (def cv (get prodsv 0))
                      (if (not= itemn cv)
                        (do
                          (recur (+ c 1)))
                        (do
                          (def oneprice (get prodsv 2))
                          (def partialvalue (* (Double/parseDouble oneprice) (Integer/parseInt pricen)))
                          (def totalvalue (+ totalvalue partialvalue))
                          ))

                      )
                    )
                  (recur (+ b 1))
                  )

                )
              )
            )
          (def totalvalue (format "%.2f" totalvalue))
          (println s ": $" totalvalue)
          )
        )

      )
    )
  )
(defn count4prod []

  (def produ (app/prod))
  (def sal (app/sales))
  (def cprodu (count produ))
  (def csalu (count sal))
  (def amount 0)
  (println "Please write the item you want to find!")
  (def ss (read-line))

  (loop [t 0]
    (when (< t cprodu))
    (def pps (get produ t))
    (def ppv (clojure.string/split pps #"\|"))
    (def pname (get ppv 1))
    (if (not= ss pname)
      (do
        (if (= (+ t 1) cprodu)
          (println "Sorry item not found!")
          (recur (+ t 1)))
        )
      (do
        (def placep (get ppv 0))
        (loop [r 0]
          (when (< r csalu)
            (def sss (get sal r))
            (def ssv (clojure.string/split sss #"\|"))
            (def sval (get ssv 2))
            (if (not= sval placep)
              (do
                (recur (+ r 1))
                )
              (do
                (def am (get ssv 3))
                (def am2 (Integer/parseInt am))
                (def amount (+ amount am2))

                (recur (+ r 1))
                )
              )
            )
          )
        (println amount)
        )
      )
    )
  )
