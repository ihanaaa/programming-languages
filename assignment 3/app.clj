(ns app)
(defn cust []

  (def cs1 (slurp "cust.txt"))
  (def cs2 (clojure.string/split-lines cs1))
  (into [ ] cs2)
  )

(defn prod []
  (def ps1 (slurp "prod.txt"))
  (def ps2 (clojure.string/split-lines ps1))
  (into [ ] ps2)
  )

(defn sales []
  (def ss1 (slurp "sales.txt"))
  (def ss2 (clojure.string/split-lines ss1))
  (into [ ] ss2)
)
