(setq inhibit-startup-message t)

(scroll-bar-mode -1)
(tool-bar-mode -1)
(set-fringe-mode 10)

;; Disable line numbers for some modes
(dolist (mode '(org-mode-hook
                term-mode-hook
                shell-mode-hook
                eshell-mode-hook))
  (add-hook mode (lambda () (display-line-numbers-mode 0))))

(org-babel-do-load-languages
 'org-babel-load-languages
 '((emacs-lisp .t)
   (python . t)))

(push '("conf-unix" . conf-unix) org-src-lang-modes)

;; Automatically tangle our Emacs.org config file when it's saved
(defun abrown/org-babel-tangle-config ()
  (when (string-equal (buffer-file-name)
                      (expand-file-name "~/Documents/projects/dotfiles/emacs/Emacs-config.org"))
    ;; Dynamic scoping to the rescue
    (let ((org-confirm-babel-evaluate nil))
      (org-babel-tangle))))

  (add-hook 'org-mode-hook (lambda () (add-hook `after-save-hook #'abrown/org-babel-tangle-config)))
