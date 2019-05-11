-module(server_network).

-compile(export_all).

-include_lib("eunit/include/eunit.hrl").

println(Str) ->
    io:fwrite("~s~n", [Str]).

accept_loop(Pid, LSock) ->
    {ok, Sock} = gen_tcp:accept(LSock),
    Pid ! {newConnection, Sock},
    sender ! {newSocket, Sock},
    accept_loop(Pid, LSock).

recv_create_loop() ->
    receive
        {newConnection, Sock} -> 
            spawn(?MODULE, do_recv, [Sock, []])
    end,
    recv_create_loop().

server() ->
    {ok, LSock} = gen_tcp:listen(6789, [binary, {packet, 0}, 
                                        {active, false}, {keepalive, true}]),
                                        
    SenderPid = spawn(?MODULE, sender, [[]]),
    register(sender, SenderPid),
    
    spawn(?MODULE, accept_loop, [self(), LSock]),
    
    recv_create_loop().

    % {ok, Sock} = gen_tcp:accept(LSock),
    % {ok, Bin} = do_recv(Sock, []),
    % ok = gen_tcp:close(Sock),
    % ok = gen_tcp:close(LSock),
    % Bin.

do_recv(Sock, Bs) ->
    case gen_tcp:recv(Sock, 0) of
        {ok, B} ->
            io:fwrite("packet: ~p~n", [B]),
            sender ! {data, Sock, B}, 
            do_recv(Sock, [Bs, B]);
        {error, closed} ->
            println("CLOSED"),
            sender ! {closedSocket, Sock},
            {ok, list_to_binary(Bs)}
    end.

do_send(Sock, B) ->
    ok = gen_tcp:send(Sock, B).

sender(Sockets) ->
    %io:fwrite("Sender ~p~n", [Sockets]),
    receive
        {data, From, B} ->
            % [do_send(Sock, B) || Sock <- Sockets, From /= Sock];
            [do_send(Sock, B) || Sock <- Sockets];
        {newSocket, S} ->
            sender([S | Sockets]);
        {closedSocket, Sock} ->
            L = lists:delete(Sock, Sockets),
            sender(L)
    end,
    sender(Sockets).