;1f
(define bar 1)
;cdr fjerner det første elementet og retunerer en ny liste. car henter første elementet fra den ny1 listen
; (0 42 #t bar) -> (42 #t bar) -> 42
(car(cdr (list 0 42 #t)))

;1g && 1i
;definerer liste. Viser samtidig hvordan man kan lage listen med bare list
(define foo(list (list 0 42) (list #t bar)))

;henter først den først den  "nestede listen"[0] cved hjelp av car. henter deretter listen [42:] ved hjelp av cdr. Deretter henter jeg 42 ved hjelp av car  som henter første element
; (0 42) -> (42 ) -> 42
(car(cdr(car foo)))

;1h
;definerer liste. 
(define koo(list 0 (list 42 #t) (list bar)))
; 42 er i nestedlist 2 , altså indeks [1]. lager ny liste uten første element ved hjelp av cdr, deretter henter jeg liste [42] ved hjelp av car. Deretter henter jeg første element ved hjelp av car igjen
; (42 #t) -> (42 ) -> 42
(car(car (cdr koo)))

;1i cons
; Viser hvordan man kan lage  listen i g ved hjelp av cons. Legger til emty string for å fjerne punktum mellom tallene. 
(define zoo(cons (cons 0 (cons 42 '())) (cons (cons #t (cons bar '())) '())))
foo
zoo

;2a
(define (take n lst)
;Sjekker om enten n = 0 eller lst= 0 OG om at lengden av listen er større enn n
  (if (and (or(= n 0) (null? lst))(> (length lst ) n))                 
         '()
         ;bygger opp ett rekurivt kall som stoppes når if sjekken ovenfor kjører.
         (cons (car lst)            
               (take (- n 1)(cdr lst))))) 

(define l (list 'a 'b 'c 'd))

(take 2 l)

;2b
(define (take2 n lst)
; reverserer listen og fjerner elementet. reverserer det tilbake før rekurserer tibake
      (if (< (length lst) (+ 1 n))
        lst 
        (take2 n (reverse (cdr(reverse lst)))))) 
        
(take2 2 l)

;2c
(define (take-while pred lst)
  ;programmet stoppes når listen som sendes inn er 0, altså den er ferdig traverset gjennom elementene
  (if (null? lst)
      '()
      ;sjekker om første elemenet i lista har egenskap pred
      (if (pred (car lst))
          ;hvis ja, bygger jeg opp ett rekusrsivt kall
          (cons (car lst) (take-while pred (cdr lst)))
          ;hvis ikke så stoppes programmet
          '())))

(take-while even? '(2 34 42 56 66))

;2d
;Tar inn 3 argumenter, operatoren, list 1, list2
(define (map2 operator lst1 lst2)
  ;sjekker om begge listene har en lengde over 0. Hvis ikke så er det ikke noe mer å regne, så programme stoppes 
  (if(and (> (length lst1 ) 0) (> (length lst2 ) 0))
    ;bygger opp en string hvor det regner første element og hvor andre elementet er rekursivt, så det bygges opp i andre posisjon
        (cons (operator (car lst1) (car lst2)) (map2 operator (cdr lst1) (cdr lst2)))
       '() )
  )
;2e
;lambda (x y) (/ (+ x y ) 2)
(map2 (lambda (x y) (/ (+ x y ) 2)) '(1 2 3 4) '(3 4 5))


