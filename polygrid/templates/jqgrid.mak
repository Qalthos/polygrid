<div>
  <div class="gridfooter" align="right">
    % if w.model:
        % if w.model.__name__ in graphs:
          <a href="#" onclick="civx_new_tab_iframe('#${w.model.__name__}_metrics', '${w.model.__name__} Metrics', '/topN/${w.model.__name__}'); return false;"><span class="ss_sprite ss_chart_bar">Metrics</span></a>
          <a href="/feeds/${w.model.__name__}"><span class="ss_sprite ss_feed">Feed</span></a>
          <a href="/documentation/models/${w.model.__name__}"><span class="ss_sprite ss_report">Docs</span></a>
        % endif
        % if w.git_repo:
          <a href="#" onclick="civx_new_tab_iframe('#${w.model.__name__}_raw', '${w.model.__name__} Raw Data', '${w.gitweb}/?p=civx-csv&a=tree&f=${w.git_repo}'); return false;"><span class="ss_sprite ss_page_white_text">Raw</span></a>
        % endif
        <a href="#" onclick="moksha.view_module_source('${w.model_module}'); return false;"><span class="ss_sprite ss_database_gear">Model Source</span></a>
        <a href="#" onclick="moksha.view_module_source('${w.scraper_module}'); return false;"><span class="ss_sprite ss_script_gear">Scraper Source</span></a>
        <a href="#" onclick="moksha.view_module_source('${w.gridname}'); return false;"><span class="ss_sprite ss_brick">Widget Source</span></a>
        <a href="#" onclick="civx_new_tab('#Attribution', 'Attribution', '/widgets/entourage'); return false;"><span class="ss_sprite ss_information">Attribution</span></a>
        <a href="#" onclick="civx_embed_widget_dialog('${w.gridname}'); return false;"><span class="ss_sprite ss_html_add">Embed</span></a>
    % endif
  </div>
  <br/>
  <table id="${w.id}" class="scroll" cellpadding="0" cellspacing="0"></table>
  <div id="${w.id}_pager" class="scroll" style="text-align:center;"></div>
</div>
