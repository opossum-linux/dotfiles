if status is-interactive
    # Commands to run in interactive sessions can go here
 end


 # Use powerline/patched fonts for proper separators
set -g theme_powerline_fonts true

# Show command duration when long-running (seconds)
set -g theme_display_cmd_duration true
set -g theme_cmd_duration_threshold 5  # show if >5s

# Prompt segments order: elements are 'ssh','user','host','dir','git','hg','jobs','battery','time'
# Default is fine; to customize:
set -g theme_display_user yes
set -g theme_display_host no
set -g theme_display_vc_branch yes
set -g theme_display_jobs yes

# Colors: use ANSI color names or hex (requires fish 3.0+)
set -g theme_color_success green
set -g theme_color_failure red
set -g theme_color_neutral cyan

# Git segment behavior
set -g theme_vcs_show_untracked yes
set -g theme_vcs_show_stash_count yes

# Truncate long paths and set max length
set -g theme_dir_max_length 3
set -g theme_dir_truncate_to_home yes

# Show battery and time
set -g theme_display_battery yes
set -g theme_display_time yes
set -g theme_time_format '%H:%M'

# Custom right prompt content (example shows exit status on right)
function fish_right_prompt
    if test $status -ne 0
        echo -n (set_color red)"✖ "(set_color normal)$status
    end
end

