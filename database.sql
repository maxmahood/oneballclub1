-- Run in your own Supabase SQL editor. Do not expose the service-role key in HTML.
create table if not exists public.obc_events (
 id bigint generated always as identity primary key,
 event_type text not null check (event_type in ('outbound_click','trip_add')),
 listing_id integer not null check (listing_id between 0 and 63),
 created_at timestamptz not null default now()
);
alter table public.obc_events enable row level security;
-- No public policies: browser users cannot read or write this table.
-- Netlify function uses the server-side service role key.
create index if not exists obc_events_created_at_idx on public.obc_events(created_at);
-- Example owner query:
-- select listing_id,event_type,count(*) from public.obc_events group by 1,2 order by 3 desc;
