<div>
  <div class="gridfooter" align="right">
    ## TODO:
    ## - render custom links from facts about the entity

    <ul>
        % if entity:
            <h1>${entity.title}</h1>
            <h2>Facts</h2>
            % for fact in entity.facts:
                % if entity[fact].startswith('http'):
                    <li><b>${fact}:</b> <a href="${entity[fact]}">${entity[fact]}</a></li>
                % else:
                    <li><b>${fact}:</b> ${entity[fact]}</li>
                % endif
            % endfor
         % endif
    </ul>
  </div>
  <br/>
  <table id="${id}" class="scroll" cellpadding="0" cellspacing="0"></table>
  <div id="${id}_pager" class="scroll" style="text-align:center;"></div>
</div>
