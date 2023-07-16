;; automatically generated stuff
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("b64a60e69617b4348d0402fad2f0d08a694301132e7ab243dab4d6a65c3bf948" "e3daa8f18440301f3e54f2093fe15f4fe951986a8628e98dcd781efbec7a46f2" "631c52620e2953e744f2b56d102eae503017047fb43d65ce028e88ef5846ea3b" "02f57ef0a20b7f61adce51445b68b2a7e832648ce2e7efb19d217b6454c1b644" "680f62b751481cc5b5b44aeab824e5683cf13792c006aeba1c25ce2d89826426" "da75eceab6bea9298e04ce5b4b07349f8c02da305734f7c0c8c6af7b5eaa9738" default))
 '(doom-modeline-lsp t)
 '(package-selected-packages
   '(ef-themes solaire solaire-mode highlight-parentheses emojify visual-fill-column orderless evil-magit mode-line-bell doom-themes org-bullets rainbow-delimiters use-package))
 '(warning-suppress-types '((use-package))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;; macOS fixes
(setq mac-option-key-is-meta nil)
(setq mac-command-key-is-meta t)
(setq mac-command-modifier `meta)
(setq mac-option-modifier nil)

(scroll-bar-mode -1)
(tool-bar-mode -1)


;; The default is 800 kilobytes.  Measured in bytes.
(setq gc-cons-threshold (* 50 1000 1000))

(defun efs/display-startup-time ()
  (message "Emacs loaded in %s with %d garbage collections."
           (format "%.2f seconds"
                   (float-time
                     (time-subtract after-init-time before-init-time)))
           gcs-done))

(add-hook 'emacs-startup-hook #'efs/display-startup-time)

;; Disable line numbers for some modes
(dolist (mode '(org-mode-hook
		term-mode-hook
		shell-mode-hook
		eshell-mode-hook
    mastodon-mode-hook
    treemacs-mode-hook
    erc-mode-hook))
  (add-hook mode (lambda () (display-line-numbers-mode 0))))

;; Make ESC quit prompts
(global-set-key (kbd "<escape>") 'keyboard-escape-quit)

;; Initiliaze package sources
(setq-default
 package-native-compile t
 use-package-always-defer t
 use-package-always-ensure t)

(require 'package)
(require 'use-package)

(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") 'append)
(add-to-list 'package-archives '("elpa" . "https://elpa.gnu.org/package/")'append)

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

;; Init use-package on non-Linux platforms
(unless (package-installed-p 'use-package)
  (package-install 'use-package))


;; Setting some options for line numbers and setq
(setq-default display-line-numbers 'visual
              display-line-numbers-widen t
              ;; this is the default
              display-line-numbers-current-absolute t)

(defun noct-relative ()
  "Show relative line numbers."
  (setq-local display-line-numbers 'visual))

(defun noct-absolute ()
  "Show absolute line numbers."
  (setq-local display-line-numbers t))

(add-hook 'evil-insert-state-entry-hook #'noct-absolute)
(add-hook 'evil-insert-state-exit-hook #'noct-relative)
;; example of customizing colors
;; (custom-set-faces '(line-number-current-line ((t :weight bold
;;                                                  :foreground "goldenrod"
;;                                                  :background "slate gray"))))

;; vim-like scrolloff margin and scrolling
(setq scroll-margin 8)
(setq scroll-step 1)

;; consolidate backups into one place instead of all over my hard drive
(setq
   backup-by-copying t      ; don't clobber symlinks
   backup-directory-alist
   `(("." . ,(concat user-emacs-directory "backups")))
   delete-old-versions t
   kept-new-versions 6
   kept-old-versions 2
   version-control t)       ; use versioned backups

;; when auto-saving, just save the file itself. don't make a new file
(setq auto-save-visited-mode t)

;; save history in minibuffers
(setq history-length 100)
(savehist-mode 1)
(save-place-mode 1)

(hl-line-mode 1)
;; Revert buffers when the underlying file has changed. aka when it gets changed somewhere else
(global-auto-revert-mode 1)
(setq global-auto-revert-non-file-buffers t)

;; Don't warn when following symlinnked files
(setq vc-follow-symlinks t)

;; spaces instead of tabs for indentation
(setq-default indent-tabs-mode nil)

(use-package paren
  :ensure nil
  :init
  (show-paren-mode +1)
  :config
  (setq show-paren-delay 0))

;; (use-package highlight-parentheses
;;   :init
;;   (highlight-parentheses-mode)
;;   :config
;;   (setq highlight-parentheses-delay 0)
;;   )

(use-package mode-line-bell
  :init (mode-line-bell-mode 1))


(use-package vertico
  :bind (:map vertico-map
              ("C-j" . vertico-next)
              ("C-k" . vertico-previous)
              ("C-f" . vertico-exit)
              :map minibuffer-local-map
              ("M-h" . backward-kill-word))
  :custom
  (vertico-cycle t)
  (setq vertico-count 20)
  :init
  (vertico-mode))


(use-package marginalia
  :after vertico
  :bind
  ("M-A" . marginalia-cycle)
  ;; :custom
  ;; (marginalia-annotators '(marginalia-annotators-heavy marginalia-annotators-light nil))
  :init
  (marginalia-mode))


(use-package orderless
  :custom
  (completion-styles '(orderless basic))
  (completion-category-overrides '((file (styles basic partial-completion)))))


(use-package all-the-icons)


(use-package doom-modeline
  :custom
  (doom-modeline-height 30)
  (setq doom-modeline-time t)
  (setq doom-modeline-battery t)
  (setq doom-modeline-minor-modes t)
  :init (doom-modeline-mode 1)
  )


(use-package doom-themes
  :config
  (doom-themes-visual-bell-config)
  :init (load-theme 'doom-material-dark t))

(solaire-global-mode +1)
(add-to-list 'solaire-mode-themes-to-face-swap 'doom-material-dark)


(use-package rainbow-delimiters
  :hook (prog-mode . rainbow-delimiters-mode))


(use-package which-key
  :init (which-key-mode)
  :diminish which-key-mode
  :config
  (setq which-key-idle-delay 1))


(use-package helpful)
;; Note that the built-in `describe-function' includes both functions
;; and macros. `helpful-function' is functions only, so we provide
;; `helpful-callable' as a drop-in replacement.
(global-set-key (kbd "C-h f") #'helpful-callable)

(global-set-key (kbd "C-h v") #'helpful-variable)
(global-set-key (kbd "C-h k") #'helpful-key)
(global-set-key (kbd "C-h x") #'helpful-command)

;; Lookup the current symbol at point. C-c C-d is a common keybinding
;; for this in lisp modes.
(global-set-key (kbd "C-c C-d") #'helpful-at-point)

;; Look up *F*unctions (excludes macros).
;;
;; By default, C-h F is bound to `Info-goto-emacs-command-node'. Helpful
;; already links to the manual, if a function is referenced there.
(global-set-key (kbd "C-h F") #'helpful-function)


(use-package general
  :config
  (general-create-definer abrown/leader-keys
    :keymaps `(normal visual emacs)
    :prefix "SPC"
    :global-preFix "C-SPC")

  (abrown/leader-keys
    "t" '(:ignore t :which-key "toggles")
    "tw" 'whitespace-mode
    "tt" '(load-theme :which-key "choose theme")
    "f" '(project-find-file :which-key "find file in project")
    "o" '(project-switch-project :which-key "find file in project")
    ;; "ff" '(project-find-file :which-key "find file")))
    "def" '(lambda () (interactive) (find-file (expand-file-name "~/.emacs.d/init.el")))
  ))


(use-package evil
  :init
  (setq evil-want-integration t)
  (setq evil-want-keybinding nil)
  (setq evil-want-C-u-scroll t)
  (setq evil-want-C-i-jump t)
  (evil-mode 1)
  (define-key evil-insert-state-map (kbd "C-g") 'evil-normal-state)
  (define-key evil-insert-state-map (kbd "C-h") 'evil-delete-backward-char-and-join)

  ;; Use visual line motions even outside of visual-line-mode buffers
  (evil-global-set-key 'motion "j" 'evil-next-visual-line)
  (evil-global-set-key 'motion "k" 'evil-previous-visual-line)
  (evil-global-set-key 'motion "0" 'evil-first-non-blank)

  (evil-set-initial-state 'messages-buffer-mode 'normal)
  (evil-set-initial-state 'dashboard-mode 'normal))
  

(use-package evil-collection
  :after evil
  :config
  (evil-collection-init))

;; disable evil in some modes
(dolist (mode '(mastodon-mode))
 (add-to-list 'evil-emacs-state-modes mode))

(defun my-center-line (&rest _)
  (evil-scroll-line-to-center nil))

(dolist (evil-functions '(evil-scroll-up
                          evil-scroll-down
                          evil-search-next
                          evil-search-previous))
  (advice-add evil-functions :after #'my-center-line))

;; tab widths
(setq-default tab-width 2)
(setq-default evil-shift-width 2)

(use-package goto-chg)

(use-package magit
  :commands magit-status)


;; Org-mode stuff
(defun abrown/org-mode-setup ()
  (org-indent-mode)
  ;(variable-pitch-mode 1)
  (visual-line-mode 1))

(use-package org
  :hook (org-mode . abrown/org-mode-setup)
  :config
  (setq org-ellipsis " ▾")
  (setq org-agenda-start-with-log-mode t)
  (setq org-log-done 'time)
  (setq org-log-into-drawer t)

  (setq org-agenda-files
	'("~/Documents/projects/emacs/OrgFiles/tasks.org"
	  "~/Documents/projects/emacs/OrgFiles/journal.org"
	  "~/Documents/projects/emacs/OrgFiles/habits.org")))

  (require 'org-habit)
  (add-to-list 'org-modules 'org-habit)
  (setq org-habit-graph-column 60)

  (setq org-capture-templates
    `(("t" "Tasks / Projects")
      ("tt" "Task" entry (file+olp "~/Documents/projects/emacs/OrgFiles/tasks.org" "Inbox")
           "* TODO %?\n  %U\n  %a\n  %i" :empty-lines 1)

      ("j" "Journal Entries")
      ("jj" "Journal" entry
           (file+olp+datetree "~/Documents/projects/emacs/OrgFiles/journal.org")
           "\n* %<%I:%M %p> - Journal :journal:\n\n%?\n\n"
           ;; ,(dw/read-file-as-string "~/Notes/Templates/Daily.org")
           :clock-in :clock-resume
           :empty-lines 1)
      ("jm" "Meeting" entry
           (file+olp+datetree "~/Documents/projects/emacs/OrgFiles/journal.org")
           "* %<%I:%M %p> - %a :meetings:\n\n%?\n\n"
           :clock-in :clock-resume
           :empty-lines 1)))

  (define-key global-map (kbd "C-c j")
    (lambda () (interactive) (org-capture)))

(use-package org-bullets
  :after org
  :hook (org-mode . org-bullets-mode)
  )

(defun abrown/org-mode-visual-fill ()
  (setq visual-fill-column-width 100
	visual-fill-column-center-text t)
  (visual-fill-column-mode 1)
  )

(use-package visual-fill-column
  :hook
  (org-mode . abrown/org-mode-visual-fill)
  (mastodon-mode . abrown/org-mode-visual-fill)
  )

(with-eval-after-load 'org
  (require 'org-tempo)

  (add-to-list 'org-structure-template-alist '("sh" . "src shell"))
  (add-to-list 'org-structure-template-alist '("el" . "src emacs-lisp"))
  (add-to-list 'org-structure-template-alist '("py" . "src python"))
  )

;; ;; LSP stuff
;; open python files in tree-sitter mode
(add-to-list 'major-mode-remap-alist `(python-mode . python-ts-mode))

;; (use-package eglot
;;   :hook (python-ts-mode . eglot-ensure)
;;   )

(use-package corfu
  :custom
  (corfu-cycle t)
  (corfu-auto t)
  :hook (prog-mode . corfu-mode)
  :init
  (global-corfu-mode)
  )

(use-package treemacs)
(use-package treemacs-evil)

(setq completion-category-overrides '((eglot (styles orderless))))

;; Mastodon
(use-package mastodon
  :config
  (mastodon-discover)
  (setq mastodon-active-user "powerllama")
  (setq mastodon-instance-url "https://duck.haus"))

;; (set-face-attribute 'show-paren-match nil :background "gray")

;; Emojify
(use-package emojify
  :hook (after-init . global-emojify-mode))

;; Make gc pauses faster by decreasing the threshold.
(setq gc-cons-threshold (* 8 1024 1024))

;; (use-package ef-themes)
;; (load-theme 'ef-autumn :no-confirm)

(add-to-list 'default-frame-alist '(alpha-background . 0.1))
