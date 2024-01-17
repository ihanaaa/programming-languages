(ns menu
  (:require [db]))

(defn pmenu []
  (println "*** Sales Menu ***")
  (println "------------------\n")

  (println "1. Display Customer Table")
  (println "2. Display Product Table")
  (println "3. Display Sales Table")
  (println "4. Total Sales for Customer")
  (println "5. Total Count for Product")
  (println "6. Exit\n")
  (println "Enter an option?")
  (def choice (read-line))

  (if (= choice (str "1" ""))
    (do
      (db/loadCTable)
      (println "\n")
      (pmenu)
      )
    (do
      (if (= choice (str "2" ""))
        (do
          (db/loadPTable)
          (println "\n")
          (pmenu)
          )
        (do
          (if (= choice (str "3" ""))
            (do
              (db/loadSTable)
              (println "\n")
              (pmenu)
              )
            (do
              (if (= choice (str "4" ""))
                (do
                  (db/sales4cust)
                  (println "\n")
                  (pmenu)
                  )
                (do
                  (if (= choice (str "5" ""))
                    (do
                      (db/count4prod)
                      (println "\n")
                      (pmenu))
                    (do
                      (if (= choice (str "6" ""))
                        (println "Thank you for using our Sales Order! Until next time!")
                        (println "does not work"))
                      )
                    )  ))



              )
            )
          )))))

(pmenu)
