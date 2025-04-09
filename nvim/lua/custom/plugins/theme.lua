return {
  "catppuccin/nvim",
  name = "catppuccin",
  lazy = false,
  priority = 1000,

  config = function()
    require("catppuccin").setup {
      flavour = "auto",
      integrations = {
        blink_cmp = true,
        cmp = true,
        neotree = {
          enabled = true,
          show_root = true,
          transparent_panel = false,
        },
      }
    }
    vim.cmd("colorscheme catppuccin")
  end
}
