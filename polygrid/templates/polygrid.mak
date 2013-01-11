<div>
  <div class="gridfooter" align="right">
    ## TODO:
    ## - render custom links from facts about the entity

    <ul>
        % if w.entity:
            <h1>${w.entity.name}</h1>
            <h2>Facts</h2>
            % for fact in w.entity.facts:
                % if w.entity[fact].startswith('http'):
                    <li><b>${fact}:</b> <a href="${w.entity[fact]}">${w.entity[fact]}</a></li>
                % else:
                    <li><b>${fact}:</b> ${w.entity[fact]}</li>
                % endif
            % endfor
         % endif
    </ul>
  </div>
  <br/>
  <table id="${w.id}" class="scroll" cellpadding="0" cellspacing="0"></table>
  <div id="${w.id}_pager" class="scroll" style="text-align:center;"></div>
</div>
