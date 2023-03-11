;; Since Emacs 27, an early configuration file early-init.el can be provided to
;; handle initialization to be done before init.el is loaded.

;;; Code:

(when (getenv-internal "DEBUG")
  (setq-default
   debug-on-error t
   init-file-debug t))

(setq-default
 load-prefer-newer t                    ; Avoid old byte-compiled dependencies
 mode-line-format nil)                  ; Less flickering and speed optimization

(setq-default
 inhibit-startup-message t
 default-frame-alist
 '((background-color . "#3F3F3F")       ; Default background color
   (bottom-divider-width . 1)           ; Thin horizontal window divider
   (foreground-color . "#DCDCCC")       ; Default foreground color
   ;; (fullscreen . maximized)             ; Maximize the window by default
   (horizontal-scroll-bars . nil)       ; No horizontal scroll-bars
   (left-fringe . 8)                    ; Thin left fringe
   (menu-bar-lines . 0)                 ; No menu bar
   (right-divider-width . 1)            ; Thin vertical window divider
   (right-fringe . 8)                   ; Thin right fringe
   (tool-bar-lines . 0)                 ; No tool bar
   ;; (undecorated . t)                    ; Remove extraneous X decorations
   (vertical-scroll-bars . nil)))       ; No vertical scroll-bars



;; set initial size of window
(setq initial-frame-alist
      (append initial-frame-alist
              '((width . 250)
                (height . 80))))
;;; early-init.el ends here
